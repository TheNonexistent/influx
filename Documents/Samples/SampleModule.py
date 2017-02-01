class infmod:
	#Influx Section
   def __init__(self):
       self.name = "Module Name"
       self.description = "This Module Is A Test Module For Influx. Everything Will Be Included Later"
       self.parameters = {"LocalAddress":None, "RemoteAddress":None, "Port":None}
       #"None" Is Developer's Empty Parameter. Influx Won't Avoid Running If One Of The Parameters Are This Type.
       #None Is Influx's Empty Parameter. Influx Will Avoid Running If One Of The Parameters Are This Type.
	   #...

   def __str__(self):
       return "[" + self.name + "] Influx Module Object."

   def run(self):
	   influx_module_main(self.parameters)


def influx_module_main(prams):
    #Developer Section
    influx_module = infmod
    print(influx_module)
    print("Module Ran Succesfully. Received Prameters Are:")
    for Key in prams.keys():
    	print(str(Key) + " : " + str(prams[Key]))
