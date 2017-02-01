#!/usr/bin/env python2
from __future__ import print_function
import sys,os
import readline

#Influx Default Modules Import
from Modules.Commands import *
from Modules.InfluxPrint import *
from Modules.InfmodHandler import *

##Functions##

##Functions##

#InProgram Variables
module_name = "Home"
influx_path = str(os.path.realpath(__file__)).split('/')
influx_path = '/'.join(influx_path[:-1])

#Main Part
print(Status["INFO"] + "Influx Started.")
print("")
infCommands = Commands(False, influx_path,None)
infCommands.Show_Banner()
try:
   while True:
      command = ""
      command = raw_input(Color["BLUE"] + "inf" + Color["ENDC"] + ":[" + Color["GREEN"] + module_name + Color["ENDC"] + "]>")
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
