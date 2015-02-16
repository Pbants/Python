from Tkinter import *
from sys import exit
import tkSimpleDialog
import tkMessageBox


class ConverterButtons:

	def __init__(self, master):
		frame = Frame(master)
		frame = frame.grid()

		#Create two entries, one for the temperature and one for the temperature to convert to
		Etemp = Entry(master)
		Etype = Entry(master)

		#Align the entries so they will be next to the labels
		Etemp.grid(row=0,column=1)
		Etype.grid(row=1,column=1)

		#Insert default values into the entries
		Etemp.insert(0, 0)
		Etype.insert(0, "F or C")

		#Create Two labels next to the entries
		Label(master, text="Temperature to convert").grid(row=0)
		Label(master, text="What would you like to convert it to? (F or C)").grid(row=1)

		#When button is pashed pass the vlues for the two entries to TempConvert method, convert Etemp to an int
		self.convertbutton = Button(frame, text="Convert", command=lambda :self.TempConvert(int(Etemp.get()), Etype.get()))
		self.convertbutton.grid(row=3)

		self.quitbutton = Button(frame, text="QUIT", command=exit)
		self.quitbutton.grid(row=3,column=1)

	def TempConvert(self,temp, Convert_To ):

		#Convert to celsius method
		def Convert_To_Celsius (Original_Temp):
			#Take the original temperature and convert it to Celsius
			temp_c = (float(5)/9) * (Original_Temp - 32)
			tkMessageBox.showinfo("Result", "%s is the temperature in Celsius" % (format(temp_c, '.2f')))

		#Convert to Farenheight method
		def Convert_To_Farenheight (Oringal_Temp):
			#Take the original temperature and convert it to Farenheight 
			temp_f = (float(9)/5) * Oringal_Temp + 32
			tkMessageBox.showinfo("Result", "%s is the temperature in Farenheight" % (format(temp_f, '.2f')))

		#Determine what temperature the user would like to convert to, only handles "F" or "C" (not case sensitive)
		if Convert_To.upper() == "F":
			Convert_To_Farenheight(temp)
		elif Convert_To.upper() == "C":
			Convert_To_Celsius(temp)
		else:
			print "Invalid input"
			exit(0)


root = Tk()
Con = ConverterButtons(root)
root.mainloop()
