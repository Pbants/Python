from Tkinter import *
import time
import praw
from sys import exit

class RedditCrawler:
	def __init__(self, master):
		frame = Frame(master)
		frame = frame.grid()
		
		#Add two entries for subreddit and Post Number to return
		SubEntry = Entry(master)
		PostNum = Entry(master)
		Category = Entry(master)

		SubEntry.grid(row=0,column=1)
		PostNum.grid(row=1,column=1)
		Category.grid(row=3,column=1)

		#Insert Default Values
		SubEntry.insert(0, 'Please Enter subreddit')
		PostNum.insert(0, "Enter number of posts to return")
		Category.insert(0, "Enter Category (Hot or New")

		#Create Labels next to the Entries
		Label(master, text="Please Enter Subreddit").grid(row=-0)
		Label(master, text="Please Enter Number of Posts to return").grid(row=1)
		Label(master, text="Please enter category (Hot or New)").grid(row=3)


		#Create Buttons
		self.Getbutton = Button(frame, text = "Let's go crawling!", command=lambda :self.GetSubmissions(SubEntry.get(), int(PostNum.get()), Category.get()))
		self.Getbutton.grid(row=3)

	def GetSubmissions(sub,limit,cat):
		user_agent = "User-Agent: Crawl /r/gardening test v1 by /u/comtb"
		r = praw.Reddit(user_agent=user_agent)
		r.login(username='comtb')
		while True:
			for submission in sub.get_cat(limit = 5):
				print submission.title
				print submission.url
		time.sleep(1800)
root = Tk()
RC = RedditCrawler(root)
root.mainloop()

