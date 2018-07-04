import readline
import traceback
import importlib
#Influx Default Modules Import
#from Modules.Commands import *
from Modules.InfluxPrint import *
from Modules.Commands import *
from Modules.InfluxExceptions import *
from Modules.Config import *

#InProgram Variables
influx_path = str(os.path.realpath(__file__)).split('/')
influx_path = '/'.join(influx_path[:-2])

#Module Handler Function
def InfmodHandler(module_name, module_path):
   #debugging_mode = False #Make In Dynamic So The User Can Decide Wheather Or Not It Should Be On(done)
   module_running = False
   print("")
   try:
       pos = "Infmod." + module_name.split('/')[0] + "." + module_name.split('/')[1]
       imported_infmod = importlib.import_module(pos)
       #imported_infmod = __import__(pos)
       #eval('from {0} import *'.format(pos))
       #inf_mod = __import__(pos, fromlist=['*'])
       influx_module = imported_infmod.infmod()
       print("")
       print(Status["INFO"] + "Module '" + module_name + "' Loaded Successfully.")
       print(influx_module.description)
       print("")
       modCommands = Commands(True, influx_path, influx_module, module_name)
       retval = False
   except Exception as e:
       print("")
       print(Status["ERROR"] + "Cannot Load Module.(Returning To Home.)")
       if debugging_mode == True:
          print("")
          print(Status["INFO"] + "Debugging Mode Is On.")
          print(Status["ERROR"] + "Exception Occurred While Loading Module.")
          print(Status["INFO"] + "Exception:")
          print("          " + repr(e))
          print(Status["INFO"] + "Full TraceBack:")
          print("          " + str(traceback.format_exc()))
       retval = True
   while True:
      try:
         if retval == True:
            print("")
            isdefined = [True,True,True]
            try:
                sys.modules[pos]
            except NameError:
                isdefined[0] = False
            try:
                import_module
            except NameError:
                isdefined[1] = False
            try:
                influx_module
            except NameError:
                isdefined[2] = False
            if isdefined[0]:
                del sys.modules[pos]
            if isdefined[1]:
                del imported_infmod
            if isdefined[2]:
                del influx_module
            print(Status["INFO"] + "Module '" + module_name + "' Unloaded")
            print("")
            break
         command = input(Color["BLUE"] + "inf" + Color["ENDC"] + ":[" + Color["GREEN"] + module_name + Color["ENDC"] + "]>")
         if command != "":
            if command == "run" or command == "exploit" or command == "execute":
               module_running = True
            if command == "reload":
               print("")
               isdefined = [True,True,True]
               try:
                   sys.modules[pos]
               except NameError:
                   isdefined[0] = False
               try:
                   import_module
               except NameError:
                   isdefined[1] = False
               try:
                   influx_module
               except NameError:
                   isdefined[2] = False
               if isdefined[0]:
                   del sys.modules[pos]
               if isdefined[1]:
                   del imported_infmod
               if isdefined[2]:
                   del influx_module
               print(Status["INFO"] + "Reloading  '" + module_name + "'.")
               print("")
               retval = modCommands.Load(module_name)
            else:
                retval = modCommands.Command(command)
            if isinstance(retval, list):
               InfmodHandler(retval[0], retval[1])
               break
      except KeyboardInterrupt:
         if module_running:
            print("")
            print("")
            print(Status["INFO"] + "Keyboard Interrupt.")
            print("")
            print("")
            module_running = False
            continue
         else:
            print("")
            print("")
            print(Status["INFO"] + "Keyboard Interrupt.")
            print(Status["INFO"] + "Exiting Influx...")
            print("")
            sys.exit(4)
      except ModuleKeyboardInterrupt:
          print("")
          print("")
          print(Status["INFO"] + "Keyboard Interrupt.")
          print("")
          print("")
          module_running = False
          continue
      except StopModuleException as e:
          print("")
          print(Status["ERROR"] + "Module: [" + str(influx_module.name) + "] Ran Into An Error.")
          if debugging_mode == True:
             print("")
             print(Status["INFO"] + "Debugging Mode Is On.")
             print(Status["ERROR"] + "Exception Occurred While Running Module.")
             print(Status["INFO"] + "Exception:")
             print("          " + repr(e))
             print(Status["INFO"] + "Full TraceBack:")
             print("          " + str(traceback.format_exc()))
          print("")
          print(Status["INFO"] + "Stopping.")
          print("")
          module_running = False
      except Exception as e:
           print("")
           print(Status["ERROR"] + "Cannot Load Module.(Returning To Home.)")
           if debugging_mode == True:
              print("")
              print(Status["INFO"] + "Debugging Mode Is On.")
              print(Status["ERROR"] + "Exception Occurred While Loading Module.")
              print(Status["INFO"] + "Exception:")
              print("          " + repr(e))
              print(Status["INFO"] + "Full TraceBack:")
              print("          " + str(traceback.format_exc()))

#      except:
#          print(Status["ERROR"] + "Something Went Wrong.")
#          print(Status["INFO"] + "Stabilizing.")
#          continue
