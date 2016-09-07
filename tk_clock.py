from Tkinter import *
from datetime import datetime
from pytz import timezone
import time

#Initialize TK
root = Tk()
root.title("Current Time")
root.configure(background='black')

#Create Labels for the three timezones
mst_time = Label(root,font=('arial', 10, 'bold'),fg='green',bg='black')
mst_time.pack()
ist_time = Label(root,font=('arial', 10, 'bold'),fg='green',bg='black')
ist_time.pack()
utc_time = Label(root,font=('arial', 10, 'bold'),fg='green',bg='black')
utc_time.pack()

#get the current time for the requested timezones, requires timezone variables to be passed in
def get_curr_time():

    #Set timezones
    mst_zone= timezone('US/Mountain')
    ist_zone= timezone('Asia/Kolkata')
    utc_zone= timezone('UTC')

    #Get current times for given timezones
    mst_now= datetime.now(mst_zone)
    ist_now= datetime.now(ist_zone)
    utc_now= datetime.now(utc_zone)

    #Current times in Year-Month-Day Hour:Minute:Second format
    mst_curr= mst_now.strftime("Current MST Time:" + " " + '%Y-%m-%d'+ " " + '%H:%M:%S ')
    ist_curr= ist_now.strftime("Current IST Time:" + " " + '%Y-%m-%d'+ " " + '%H:%M:%S ')
    utc_curr= utc_now.strftime("Current UTC Time:" + " " + '%Y-%m-%d'+ " " + '%H:%M:%S ')

    #Update labels every
    mst_time.config(text=mst_curr)
    ist_time.config(text=ist_curr)
    utc_time.config(text=utc_curr)

    mst_time.after(200, get_curr_time)

get_curr_time()
root.mainloop()
