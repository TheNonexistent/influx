class infmod:
	#Influx Section
   def __init__(self):
       self.name = "Module Name"
       self.description = "This Module Is A Test Module For Influx."
       self.parameters = {"LocalAddress":None, "RemoteAddress":None, "Port":None}
       #"None"(String) Is The Developer's Empty Parameter. Influx Will Not Avoid Executing The Module If One Of The Parameters Are Of This Type.
       #None(Null) Is Influx's Empty Parameter. Influx Will Avoid Executing The Module If One Of The Parameters Are Of This Type.
	   #...

   def __str__(self):
       return "[" + self.name + "] Influx Module Object."

   def run(self):
	   influx_module_main(self.parameters)


def influx_module_main(prams):
    #Developer's Section:In This Section The Developer Of The Influx-Module Will Be Able To Receive The Parameters Given By The User Through Influx Core And Work With Them. 
    influx_module = infmod
    print(influx_module)
    print("Module Ran Succesfully. Received Prameters Are:")
    for Key in prams.keys():
    	print(str(Key) + " : " + str(prams[Key]))
	
	
if __name__ == "__main__":
    print("This File Is An Influx-Module Created To Be Imported In The Influx Core And Function Within It.")
    print("It Is Not Meant To Run On It's Own. You Can Import This Module To A Matching Influx Version.")

	
###################################################################
#Many Programs Need Files To Function. For Using Files And Directories For Your Influx-Module You Can-
#-Use The Directory (infpath/ModDb), And Create A Directory For Your Influx-Module. There Soon Will Be A Mechanism To Manage Such Needs.
###################################################################
