#!/usr/bin/env python3
from __future__ import print_function
import sys,os
import readline

#Influx Default Modules Import
from Modules.Commands import *
from Modules.InfluxPrint import *
from Modules.InfmodHandler import *
from Modules.Config import *

##Functions##

##Functions##

#InProgram Variables
module_name = "Home"


#Main Part
if len(sys.argv) >= 2:
    if sys.argv[1] == "help":
        print("")
        print(Status["INFO"] + "Use '" + sys.argv[0] + " InlfuxModule' To Start Directly With Loaded Module")
        print("")
        sys.exit()

print(Status["INFO"] + "Influx Started.")
print("")
infCommands = Commands(False, influx_path,None)
infCommands.Show_Banner()

if len(sys.argv) >= 2:
    print(Status["INFO"] + "Starting Influx With Loaded Module.")
    print("")
    loadval = infCommands.Command("load " + sys.argv[1])
    try:
      loadval
    except NameError:
      pass
    else:
       if isinstance(loadval, list):
          InfmodHandler(loadval[0], loadval[1])
try:
   while True:
      command = ""
      command = input(Color["BLUE"] + "inf" + Color["ENDC"] + ":[" + Color["GREEN"] + module_name + Color["ENDC"] + "]>")
      if command != "":
         loadval = infCommands.Command(command)
      try:
        loadval
      except NameError:
        pass
      else:
         if isinstance(loadval, list):
            InfmodHandler(loadval[0], loadval[1])
except KeyboardInterrupt:
   print("")
   print("")
   print(Status["INFO"] + "Keyboard Interrupt.")
   print(Status["INFO"] + "Exiting Influx...")
   print("")




###################################################################
# This file is part of Influx.
#
#    Influx is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Influx is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Influx.  If not, see <http://www.gnu.org/licenses/>.
###################################################################
