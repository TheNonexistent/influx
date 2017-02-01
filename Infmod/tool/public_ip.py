from json import load
from urllib2 import urlopen
import sys
import os

#Influx Default Modules Import
Modules_Path = os.path.abspath(os.path.join('..', '..', 'Modules'))
sys.path.append(Modules_Path)
from Modules.InfluxPrint import *


class infmod:
   #Influx Section
   def __init__(self):
       self.name = "Public Ip Grabber"
       self.description = "This Module Will Show Your Public IP Address"
       self.parameters = {}
      #...

   def __str__(self):
       return "[" + self.name + "] Influx Module Object."

   def run(self):
      influx_module_main(self.parameters)

def influx_module_main(prams):
   print(Status["JOB"] + "Trying To Fetch Ip Address")
   pub_ip = getip()
   if pub_ip == False:
      print(Status["ERROR"] + "Failed To Fetch Ip Address.")
   else:
      print(Status["INFO"] + "Your Public Ip Address Is: [" + pub_ip + "]")

def getip():
      try:
         public_ip = urlopen('http://ip/42/pl/raw').read()
      except Exception:
         try:
            public_ip = load(urlopen('http://httpbin.org/ip'))['origin']
         except Exception:
            try:
               public_ip = load(urlopen('https://api.ipify.org/?format=json'))['ip']
            except Exception:
               try:
                  public_ip = load(urlopen('http://jsonip.com'))['ip']
               except Exception:
                  public_ip = False
      return public_ip
