from sys import exit

def Convert_To_Celsius (Original_Temp):
	#Take the original temperature and convert it to Celsius
	temp_c = (float(5)/9) * (Original_Temp - 32)
	print "%s is the temperature in Celsius" % (format(temp_c, '.2f'))

def Convert_To_Farenheight (Oringal_Temp):
	#Take the original temperature and convert it to Farenheight 
	temp_f = (float(9)/5) * Oringal_Temp + 32
	print "%s is the temperature in Farenheight" % (format(temp_f, '.2f'))


#The original temperature
temp = int(raw_input ("Please Enter the Temperature: "))

#What to convert to
convertto = raw_input ("What would you like to convert to? (F or C)")

if convertto.upper() == "F":
	Convert_To_Farenheight(temp)
elif convertto.upper() == "C":
	Convert_To_Celsius(temp)
else:
	print "Invalid input"
	exit(0)
