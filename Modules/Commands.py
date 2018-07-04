from __future__ import print_function
import sys, os, subprocess, random, re

#Influx Default Modules Import
from Modules.InfluxPrint import *
from Modules.Config import *

class Commands:
   #Information Variables
   influx_help = '''
   exit    Exits The Program

   help    Shows This Output

   show [banner, help, projects]
    -banner    Shows Influx Header And Banner
    -help    Shows This Output
    -projects    List Available Projects

   clear    Clears The Screen

   tree    Draws A Tree Of All Influx Modules

   load [Influx-Module]    Loads An Influx Module

   unload    Unloads A Loaded Influx Module

   reload    Reloads A Loaded Influx Module From Code On Disk And Not From Cache

   modify [Influx-Module]    Modifies An Influx-Module

   project [list, create, load, unload, adjust(When Loaded)]
    -list    List Available Projects
    -create [Project Name]    Creates New Project
    -load [Project Name/Project Path]    Loads An Existing Project
    -unload    Unloads Loaded Project
    -adjust    [Option Name] [Value]    Sets Project Settings
   '''

   influx_help_loaded = '''
   exit    Exits The Program

   help    Shows This Output

   show [banner, help, projects, parameters, info/information]
    -banner    Shows Influx Header And Banner
    -help    Shows This Output
    -projects    List Available Projects
    -parameters    Shows Influx Module Parameters
    -info/information    Shows Influx Module Information Including Description

   clear    Clears The Screen

   tree    Draws A Tree Of All Influx Modules

   load [Influx-Module]    Loads An Influx Module

   unload    Unloads A Loaded Influx Module

   reload    Reloads A Loaded Influx Module From Code On Disk And Not From Cache

   modify [Influx-Module]    Modifies An Influx-Module

   project [list, create, load, unload, adjust(When Loaded)]
    -list    List Available Projects
    -create [Project Name]    Creates New Project
    -load [Project Name/Project Path]    Loads An Existing Project
    -unload    Unloads Loaded Project
    -adjust    [Option Name] [Value]    Sets Project Settings

   parameters    Shows Influx Module Parameters

   info/information    Shows Influx Module Information Including Description

   set [Parameter Name] [Value]    Sets Value Of A Influx Module Parameter

   run/execute/exploit    Starts Running Influx Module With Given Parameters
    #
   '''

   #Multi Usage Commands
   show_command = ['show banner', 'show help', 'show projects', 'show parameters','show info', 'show information']

   #Global Variables

   ##Main Function##
   def __init__(self,s_isloaded, s_influx_path, s_influx_module, s_loaded_module_name = "not_loaded"):
      self.isloaded = s_isloaded
      self.loaded_module_name = s_loaded_module_name
      self.influx_path = s_influx_path
      self.influx_module = s_influx_module
   #Commands Function
   def Command(self,command):
      #command = command.lower()
      if command == "exit":
         print("")
         print(Status["INFO"] + "Exiting Influx...")
         print("")
         sys.exit(0)
      #Show Parser
      elif command.startswith("show"):
         isav = False
         counter = 0
         for form in self.show_command:
            if command == form:
               isav = True
               break
            counter += 1
         if isav:
           if counter == 0:
              self.Clear()
              self.Show_Banner()
           elif counter == 1:
              self.Show_Help()
           elif counter == 2:
              #Projects... Will Be Available Soon :)
              print("Projects... Will Be Available Soon :)")
           elif counter == 3:
              if self.isloaded:
                 print("")
                 print(Status["INFO"] +"Parameters For Influx Module: [" + self.influx_module.name + "]")
                 print("")
                 if self.influx_module.parameters == {}:
                    print("This Module Requires No Parameters")
                 else:
                    for Key in self.influx_module.parameters.keys():
                       print(str(Key) + " : " + str(self.influx_module.parameters[Key]))
                 print("")
              else:
                 print(Status["ERROR"] + "No Influx Module Loaded.")
           elif counter == 4 or counter == 5:
              if self.isloaded:
                 print("")
                 print(Status["INFO"] + "Module Name: " + str(self.influx_module.name))
                 print(Status["INFO"] + "Description: " + "\n" + "   " + self.influx_module.description)
                 print("")
              else:
                 print(Status["ERROR"] + "No Influx Module Loaded.")
         else:
            print(Status["ERROR"] + "Wrong Usage Of 'show' Command.")
            print(Status["INFO"] + "Usage:")
            for show in self.show_command:
               print("-" + show)
      elif command == "clear":
         self.Clear()
      elif command == "standalone":
         print("~~Creates Standalone Version Of An Infmod~~")
      elif command == "tree":
         if self.Which("tree"):
            print(Status["INFO"] + "Tree Of All Influx-Modules:\n")
            #os.system("tree Infmod")
            tree = os.popen("tree Infmod")
            for tree_line in tree:
               if tree_line.rstrip()[-11:] != "__init__.py" and tree_line.rstrip()[-4:] != ".pyc" and tree_line.rstrip()[-11:] != "__pycache__":
                  print(tree_line,end='')
         else:
            print(Status["ERROR"] + "Your System Does Not Support Tree.Or Something Went Wrong!")
            print(Status["ERROR"] + "You Can Use The 'list' Command Instead.")
            print(Status["ERROR"] + "Or You Can Install tree Package And Try Again.")
      elif command == "help":
         self.Show_Help()
      #Load Parser
      elif command.startswith("load"):
         module_n = command[5:]
         return self.Load(module_n)
      elif command == "unload":
         if self.isloaded:
            return True
         else:
            print(Status["ERROR"] + "No Influx Module Loaded.")
      elif command.startswith("modify"):
         module_n = command[7:]
         if module_n == "":
            print(Status["ERROR"] + "No Influx Module Specified.")
         else:
            module_n = re.sub(r'\b.py\b', '', module_n)
            if self.isloaded == True and self.loaded_module_name == module_n:
               print(Status["ERROR"] + "Cannot Modify Loaded Module.")
               print(Status["INFO"] + "Please Unload Or Load Another Module And Retry.")
            else:
               self.Modify(module_n)
      elif command == "list":
         print(Status["INFO"] + "List Of All Influx-Modules:\n")
         infmodes = self.Walk("Infmod")
         for infmod in infmodes:
            if infmod[len(infmod) - 1] != "__init__.py" and infmod[len(infmod) - 1][-4:] != ".pyc" and infmod[len(infmod) - 1] != ".gitignore" and infmod[len(infmod) - 1] != "__pycache__":
               print(infmod[-2] + "/" + infmod[-1][:-3])
         print("")
      #Infmod Handler Commands
      elif command == "parameters":
         if self.isloaded:
            print("")
            print(Status["INFO"] +"Parameters For Influx Module: [" + self.influx_module.name + "]")
            print("")
            if self.influx_module.parameters == {}:
               print("This Module Requires No Parameters")
            else:
               for Key in self.influx_module.parameters.keys():
                   print(str(Key) + " : " + str(self.influx_module.parameters[Key]))
            print("")
         else:
            print(Status["ERROR"] + "No Influx Module Loaded.")
      elif command.startswith("set"):
          if self.isloaded:
             sopt = command.split(' ')
             #Set Handler For Examples Like This One: set "SOmething SOmething" "SOMETHING AND sOMEHTING"
             valid_p = True
             valid_v = True
             try:
                sopt[1]
             except:
                valid_p = False
             try:
                sopt[2]
             except:
                valid_v = False
             if valid_p and sopt[1] != "":
                if valid_v and sopt[2] != "":
                   if sopt[1] in self.influx_module.parameters.keys():
                      self.influx_module.parameters[sopt[1]] = sopt[2]
                      print("")
                      print(Status["INFO"] + str(sopt[1]) + " -> " + str(sopt[2]))
                      print("")
                   else:
                      print(Status["ERROR"] + "Given Parameter Does Not Exist")
                else:
                   print(Status["ERROR"] + "No Value Given")
             else:
                print(Status["ERROR"] + "No Parameter Specified")
          else:
             print(Status["ERROR"] + "No Influx Module Loaded.")
      elif command == "run" or command == "execute" or command == "exploit":
         valid = True
         for Key in self.influx_module.parameters.keys():
            if self.influx_module.parameters[Key] == None:
               valid = False
         if valid:
             print("")
             print(Status["JOB"] + "Running Module: [" + str(self.influx_module.name) + "] With Given Parameters")
             print("")
             self.influx_module.run()
             print("")
             print(Status["INFO"] + "Module: [" + str(self.influx_module.name) + "] Ran Successfully ")
             print("")
         else:
             print(Status["ERROR"] + "Parameter(s) Not Set.")
      elif command == "info" or command == "information":
          if self.isloaded:
             print("")
             print(Status["INFO"] + "Module Name: " + str(self.influx_module.name))
             print(Status["INFO"] + "Description: " + "\n" + "   " + self.influx_module.description)
             print("")
          else:
             print(Status["ERROR"] + "No Influx Module Loaded.")
      elif command == "reload":
         print(Status["ERROR"] + "No Influx Module Loaded.")
      else:
         print(Status["ERROR"] + "Command Not Found.")

   ##Subsidiary Functionexits##
   #Show Influx Banner
   def Show_Banner(self):
      banner_id = random.randint(1,5)
      self.Clear()
      if banner_id == 1:
         print(Color["LBLUE"] + """
    ___ _   _ _____ _    _   ___  __
   |_ _| \ | |  ___| |  | | | \ \/ /
    | ||  \| | |_  | |  | | | |\  /
    | || |\  |  _| | |__| |_| |/  \\
   |___|_| \_|_|   |_____\___//_/\_\\ FrameWork [Alpha]
                                """ + Color["ENDC"])
      elif banner_id == 2:
         print(Color["LRED"] + """
    ____________   ________________ _____  _____  __
    ____  _/__  | / /__  ____/__  / __  / / /_  |/ /
     __  / __   |/ /__  /_   __  /  _  / / /__    /
    __/ /  _  /|  / _  __/   _  /___/ /_/ / _    |
    /___/  /_/ |_/  /_/      /_____/\____/  /_/|_| FrameWork [Alpha]
                               """ + Color["ENDC"])
      elif banner_id == 3:
         print(Color["LYELLOW"] + """
    ### #     # ####### #       #     # #     #
     #  ##    # #       #       #     #  #   #
     #  # #   # #       #       #     #   # #
     #  #  #  # #####   #       #     #    #
     #  #   # # #       #       #     #   # #
     #  #    ## #       #       #     #  #   #
    ### #     # #       #######  #####  #     # FrameWork [Alpha]
                                  """ + Color["ENDC"])
      elif banner_id == 4:
         print(Color["GREEN"] + """
.:: .:::     .:: .:::::::: .::       .::     .:: .::     .::
.:: .: .::   .:: .::       .::       .::     .::  .::   .::
.:: .:: .::  .:: .::       .::       .::     .::   .:: .::
.:: .::  .:: .:: .::::::   .::       .::     .::     .::
.:: .::   .: .:: .::       .::       .::     .::   .:: .::
.:: .::    .: :: .::       .::       .::     .::  .::   .::
.:: .::      .:: .::       .::::::::   .:::::    .::     .:: FrameWork [Alpha]
         """ + Color["ENDC"])
      elif banner_id == 5:
         print(Color["PURPLE"] + """
===========================================================
=    ==  =======  ==        ==  ========  ====  ==   ==   =
==  ===   ======  ==  ========  ========  ====  ===  ==  ==
==  ===    =====  ==  ========  ========  ====  ===  ==  ==
==  ===  ==  ===  ==  ========  ========  ====  ====    ===
==  ===  ===  ==  ==      ====  ========  ====  =====  ====
==  ===  ====  =  ==  ========  ========  ====  ====    ===
==  ===  =====    ==  ========  ========  ====  ===  ==  ==
==  ===  ======   ==  ========  ========   ==   ===  ==  ==
=    ==  =======  ==  ========        ===      ===  ====  =
=========================================================== FrameWork [Alpha]
         """ + Color["ENDC"])

      print("")
      print(Color["LGREEN"] + "[+]Version: " + influx_version + Color["ENDC"])
      print(Color["LGREEN"] + "[+]Created By: " + influx_author + Color["ENDC"])
      print(Color["LGREEN"] + "[+]GitLab: " + "https://gitlab.com/TheNonexistent/influx/" + Color["ENDC"])
      print(Color["LBLUE"] + "[+]Influx Modules Found: " + str(self.Count_Infmod()) + Color["ENDC"])
      print("")

   #Clear Function
   def Clear(self):
      os.system("clear")
      #print(chr(27) + "[2J")
   #Chck If A Command Exists
   def Which(self,command):
      try:
         null = open(os.devnull)
         subprocess.Popen([command], stdout=null, stderr=null).communicate()
      except OSError as e:
         if e.errno == os.errno.ENOENT:
           #For Logging System:Command Not Found.
           return False
         else:
           #For Logging System:Something Else Went Wrong.
           return False
      return True

   #Shows Influx help
   def Show_Help(self):
      if not self.isloaded:
         print(self.influx_help);
      else:
         print(self.influx_help_loaded)
   def Count_Infmod(self):
      count = 0
      for _, _, file_n in os.walk("Infmod/"):
         file_n = [f_name for f_name in file_n if f_name != "__init__.py" and f_name[-4:] != ".pyc"]
         count += len(file_n)
      return count
   def Modify(self, s_module_n):
      path = "Infmod/" + s_module_n + ".py"
      path = os.path.join(self.influx_path, path)
      if os.path.isfile(path):
         print("")
         print(Status["INFO"] + "Modifying " + s_module_n + " With Nano Text Editor:\n")
         os.system("nano " + path)
      else:
         print(Status["ERROR"] + "Influx Module Not Found.")
   def Walk(self, s_path):
      infmods = []
      infmodpath = str(os.path.join(self.influx_path, s_path))
      for path, subdirs, files in os.walk(infmodpath):
         for name in files:
            infmod = str(os.path.join(path, name))
            infmod = infmod.split('/')
            infmods.append(infmod[:])
      return infmods
   def Load(self,module_n):
       if module_n == "":
          print(Status["ERROR"] + "No Influx Module Specified.")
       else:
          module_n = re.sub(r'\b.py\b', '', module_n)
          path = "Infmod/" + module_n + ".py"
          path = os.path.join(self.influx_path, path)
          if os.path.isfile(path):
             #InfmodHandler.InfmodHandler(module_n, path)
              return [module_n, path]
          else:
             print(Status["ERROR"] + "Influx Module Not Found.")
