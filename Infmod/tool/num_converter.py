import sys
import os
#Influx Default Modules Import
Modules_Path = os.path.abspath(os.path.join('..', '..', 'Modules'))
sys.path.append(Modules_Path)
from Modules.InfluxPrint import *

class infmod:
   #Influx Section
   def __init__(self):
       self.name = "Number Convertor"
       self.description = "This Module Is Used To Convert Numbers\n   " + "Operations :\n   db : Decimal To Binary\n   bd : Binary To Decimal\n   dh : Decimal To Hexadecimal\n   hd : Hexadecimal To Decimal"
       self.parameters = {"Operation":None, "Value":None}
      #...

   def __str__(self):
       return "[" + self.name + "] Influx Module Object."

   def run(self):
      influx_module_main(self.parameters)

def dec_to_bin(x):
   return bin(x)[2:]

def bin_to_dec(x):
   return int(x, 2)

def dec_to_hex(x):
   return hex(x)[2:]

def hex_to_dec(x):
   return int(x, 16)

def influx_module_main(prams):

   op = prams["Operation"]
   value = prams["Value"]

   try:
      if op == 'db':
         value = int(value)
         binary = dec_to_bin(value)
         print(Status["INFO"] + str(value) + "(decimal) In Binary: " + str(binary))
      elif op == 'bd':
         value = str(value)
         decimal = bin_to_dec(value)
         print(Status["INFO"] + str(value) + "(binary) In Decimal: " + str(decimal))
      elif op == 'dh':
         value = int(value)
         hexadecimal = dec_to_hex(value)
         hexadecimal = hexadecimal.replace("L","")
         print(Status["INFO"] + str(value) + "(decimal) In Hexadecimal: " + str(hexadecimal))
      elif op == 'hd':
         value = str(value)
         decimal = hex_to_dec(value)
         print(Status["INFO"] + str(value) + "(hexadecimal) In Decimal: " + str(decimal))
      else:
         print(Status["ERROR"] + "Operation Not Supported.")
         print(Status["INFO"] + "Check You Input")
   except Exception:
      print(Status["ERROR"] + "Input Error!")
      print(Status["INFO"] + "Check You Input")
