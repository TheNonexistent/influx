#Print In Color
Color = {
   "LBLUE" : '\033[94m',
   "LGREEN" : '\033[92m',
   "LYELLOW" : '\033[93m',
   "LRED" : '\033[91m',
   "BLUE" : '\033[34m',
   "YELLOW" : '\033[33m',
   "RED" : '\033[31m',
   "GREEN" : '\033[32m',
   "PURPLE" : '\033[35m',
   "ENDC" : '\033[0m'
        }
#Print Status
Status = {
   "INFO" : Color["BLUE"] + "[+]" + Color["ENDC"],
   "ERROR" : Color["RED"] + "[#]" + Color["ENDC"],
   "JOB" : Color["GREEN"] + "[*]" + Color["ENDC"],
}
