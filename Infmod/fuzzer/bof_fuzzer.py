import sys
import os
import traceback
#Influx Default Modules Import
Modules_Path = os.path.abspath(os.path.join('..', '..', 'Modules'))
sys.path.append(Modules_Path)
from Modules.InfluxPrint import *
from Modules.InfluxExceptions import *

class infmod:
   #Influx Section
   def __init__(self):
       self.name = "Buffer Overflow Fuzzer"
       self.description = "This Module Will Create Buffers For Fuzzing Buffer Overflow Vulnerable Applications.\n" + "Output Parameter :\n   screen(Default) : Show On Screen \n   file : Print To File(Set The File Path If Selected)\n   both : Show On Screen And Print To File(Set The File Path If Selected)"
       self.parameters = {"Character":None, "Count":None, "Output":"screen", "FilePath":"None"}

   def __str__(self):
       return "[" + self.name + "] Influx Module Object."

   def run(self):
     influx_module_main(self.parameters)


def isset(var):
   try:
      var
   except NameError:
      return False
   return True

def influx_module_main(prams):
   char = prams["Character"]
   count = int(prams["Count"])
   op = prams["Output"]
   if op == 'screen':
      code = 1
   elif op == 'file':
      code = 2
   elif op == 'both':
      code = 3
   else:
      print(Status["ERROR"] + "Output Type Not Recognized.")
      raise StopModuleException("Output Type Not Recognized.")

   print(Status["INFO"] + "Simple Buffer Overflow Fuzzer")
   print("")
   try:
     if code == 1:
        print(Status["INFO"] + "Output:")
        print(char*count)
     elif code == 2:
        outfile = str(prams["FilePath"])
        if outfile == "None":
           raise StopModuleException("File Name Not Given")
        print(Status["JOB"] + "Writing To File:" + outfile)
        handle = open(outfile, 'w')
        handle.write(char*count)
        handle.close()
     elif code == 3:
        outfile = str(prams["FilePath"])
        if outfile == "None":
           raise StopModuleException("File Name Not Given")
        print(Status["INFO"] + "Output:")
        print(char*count)
        print("\n" + Status["JOB"] + "Writing To File:" + outfile)
        handle = open(outfile, 'w')
        handle.write(char*count)
        handle.close()
     print("")
     print(Status["INFO"] + "Job Finished!")
   except KeyboardInterrupt:
      raise ModuleKeyboardInterrupt()
   except:
      raise StopModuleException("Something Went Wrong")
