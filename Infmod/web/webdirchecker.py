import sys
import urllib

#Influx Default Modules Import
Modules_Path = os.path.abspath(os.path.join('..', '..', 'Modules'))
sys.path.append(Modules_Path)
from InfluxPrint import *

def show_help():
   print(Status["INFO"] + "Usage:")
   print(Status["INFO"] + "{0} URLFile Directory".format(sys.argv[0]))

try:
   dirc = sys.argv[2]
   with open(str(sys.argv[1]), 'r') as fp:
      for site in fp:
         site = site.strip()
         check = "http://" + site + "/" + dirc
         try:
            resp = str(urllib.urlopen(check).getcode())
            if resp.strip() == "200":
               print(check + "       " + "[OK]")
            elif resp.strip() == "400":
               print(check + "       " + "[404]")
            else:
               print(check + "       " + "[" + resp.strip() + "]")
         except KeyboardInterrupt:
   	      print("")
   	      print((Status["INFO"] +"User Interrupted The Proccess")
   	      print((Status["INFO"] +"Job Finished!")
   	      print((Status["INFO"] +"Coded By The Nonexistent")
   	      sys.exit()
         except:
            print(check + "[LookUp Faild]")
   print((Status["INFO"] + "Job Finished.")

except Exception:
   show_help()
   sys.exit(2)
