import sys
import optparse
import os

#Influx Default Modules Import
Modules_Path = os.path.abspath(os.path.join('..', '..', 'Modules'))
sys.path.append(Modules_Path)
from InfluxPrint import *

def show_help():
   print(Status.INFO + "Usage:")
   print("{0} Character Count -[Option]".format(sys.argv[0]))
   print(Status.INFO + "Options\n-s (Default:Show On Screen): Show On Screen\n-f [filename] : Print To File\n-sf [filename] : Show On Screen And Print To File")

def isset(var):
   try:
      var 
   except NameError:
      return False
   return True
code = 1
help_text = "\n" + Status.INFO + "{0} Character Count -[Option]".format(sys.argv[0])

parser = optparse.OptionParser(usage=help_text)
parser.add_option("-s", "--show", action="store_const", const="active", dest="show", help="(Default:Show On Screen): Show On Screen")
parser.add_option('-f', '--file', dest='ifile', help='Print To File')
parser.add_option('-b', '--both', dest='isfile', help='Show On Screen And Print To File')

(options, args) = parser.parse_args()

if options.show == "active":
   code=1
elif options.ifile != None:
   code=2
elif options.isfile != None:
   code=3
else:
   show_help()
   sys.exit(2)

try:
   char = sys.argv[1]
   count = int(sys.argv[2])
except Exception:
	show_help()
	sys.exit(4)

print(Status.INFO + "Simble Buffer Overflow Fuzzer")
print("")

if code == 1:
   print(Status.INFO + "Output:")
   print(char*count)
elif code == 2:
   outfile = str(options.ifile)
   print(Status.JOB + "Writing To File:" + outfile)
   handle = open(outfile, 'w')
   handle.write(char*count)
   handle.close()
elif code == 3:
   outfile = str(options.isfile)
   print(Status.INFO + "Output:")
   print(char*count)
   print("\n" + Status.JOB + "Writing To File:" + outfile)
   handle = open(outfile, 'w')
   handle.write(char*count)
   handle.close()

print("")
print(Status.INFO + "Job Finished!")
print(Status.INFO + "Coded By The Nonexistent")
   
      
