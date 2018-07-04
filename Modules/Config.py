import os,sys
import configparser

#Environment Variables
#-Influx Path Settings
influx_path = str(os.path.realpath(__file__)).split('/')
influx_path = '/'.join(influx_path[:-2])
#-Publish Info
influx_version = "0.4 Alpha (Python 3)"
influx_author = "The Nonexistent"


#Convert String To Boolean The Hard Way
#I Also Can Use Config.getboolean("Section", "Option") But The Exception Raising Would Be Harder... And It Works So...
def tobool(istring):
    if istring == "True":
        return True
    elif istring == "False":
        return False
    else:
        raise ConfigurationException("Boolean Convertion Error.(Boolean Type Option Set To Non-Boolean Value)")
        sys.exit()

#Parsing The Config File (default influx_path/InfConfig.cfg)

Config = configparser.ConfigParser()
Config.read(influx_path + "/InfConfig.cfg")

def ConfigRead(Section):
    Values = {}
    options = Config.options(Section)
    for option in options:
        try:
            Values[option] = Config.get(Section, option)
            if Values[option] == -1:
                DebugPrint("Skip: %s" % option)
        except:
            print("Exception On %s!" % option)
            raise ConfigurationException("Parsing Configuration Error.(Possible Unset Option)")
            sys.exit()
    return Values

if ConfigRead("Main")["dbgmod"] != None:
   debugging_mode = tobool(ConfigRead("Main")["dbgmod"])
else:
   raise ConfigurationException("Parsing Configuration Error.(Possible Unset Option)")
   sys.exit()
