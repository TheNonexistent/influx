from __future__ import print_function
import sys
import optparse
import os
#Influx Default Modules Import
Modules_Path = os.path.abspath(os.path.join('..', '..', 'Modules'))
sys.path.append(Modules_Path)
from Modules.InfluxPrint import *
from Modules.InfluxExceptions import *

##This Module Is Very Basic And Only Has Been Written For Test. Will Be Replaced Soon.##

class infmod:
	#Influx Section
   def __init__(self):
       self.name = "Backdoor And Payload Generator For Influx"
       self.description = "This Modull Will Generate A Backdoor From Available Backdoors With Given Information" + "\n" + show_help()
       self.parameters = {"Platform":None, "Type":None}
	   #...

   def __str__(self):
       return "[" + self.name + "] Influx Module Object."

   def run(self):
	   influx_module_main(self.parameters)


dbpath = "ModDb/backdoordb/"

pab = {'php':['uploader','command_execution'], 'python':['blind_tcp']}

def show_help():
   plathelp = "\n" + "Platform And Types:\n"
   plathelp += "\n" + "----------------"
   for key in pab:
      plathelp += "\n" + "Platform: " + key
      plathelp += "\n" + "\nTypes:"
      for t in pab[key]:
         plathelp += "\n" + "-" + t
      plathelp += "\n" + "----------------"
   return plathelp

#Platform Functions
def plat_php(Type):
   if Type == 'uploader':
      for line in open(dbpath + 'php/uploader', 'r'):
         print(line)
   elif Type == 'command_execution':
      for line in open(dbpath + 'php/command_execution', 'r'):
         print(line)
   else:
      print("\n"+ Status["ERROR"] + "Wrong Backdoor Type\n")
      raise StopModuleException("Wrong Backdoor Type")

def plat_python(Type):
   if Type == 'blind_tcp':
      print("Input The Remote Host: ", end='')
      rhost = input()
      print("Input The Remote Port[Listen Port]: ", end='')
      rport = input()
      print("")
      print("")
      counter = 1
      for line in open(dbpath + 'python/blind_tcp', 'r'):
         if counter == 3:
            print(line.rstrip() + " '" + rhost.rstrip() + "'")
         elif counter == 4:
            print(line.rstrip() + " " +rport.rstrip())
         else:
            print(line, end='')

         counter += 1
   else:
      print("\n" + Status["ERROR"] + "Wrong Backdoor Type\n")
      raise StopModuleException("Wrong Backdoor Type")
#End Of Platform Functions

def influx_module_main(prams):
    plat = prams["Platform"]
    typ = prams["Type"]

    if plat == 'php':
       print(Status["INFO"] + "Platform: " + plat)
       print(Status["INFO"] + "Type: " + typ)
       print("\n-----------------------------------------------------\n")
       plat_php(typ)
       print("\n-----------------------------------------------------\n")
    elif plat == 'python':
       print(Status["INFO"] + "Platform: " + plat)
       print(Status["INFO"] + "Type: " + typ)
       print("\n-----------------------------------------------------\n")
       plat_python(typ)
       print("\n-----------------------------------------------------\n")
    else:
       print("\n" + Status["ERROR"] + "Wrong Backdoor Platform\n")
       raise StopModuleException("Wrong Backdoor Platform")
