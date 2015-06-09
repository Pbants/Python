#Import PRAW (for reddit)
import praw
from pprint import *
import time
#Allows for colored text to be printed in terminal
from termcolor import colored, cprint

#User agent name in accordance with Reddit API
user_agent = "User-Agent: Crawl /r/gardening test v1.2 by /u/comtb"

r = praw.Reddit(user_agent=user_agent)

#set username, can also include password
r.login(username='comtb')

#input favorite reddit subs here
favorites = ['gardening']

#loop until keyboard inturrupt ctrl-c
while True:
	#Go through each subreddit in favorites and get the top 5 submissions under hot, can change to get_new
	for sub in favorites:
		subreddit = r.get_subreddit(sub)
		for submission in subreddit.get_hot(limit = 5):
			cprint (subreddit, 'red')
			print (submission.title)
			cprint (submission.url, 'magenta')
	#wait time in accordance with Reddit API
	time.sleep(1800)