"""

Using the twitter API to grab specific user data
Uses Twython to access twitter API
Reference: http://social-metrics.org/twitter-user-data/

"""

#Import Necessary python modules
import sys
import string
import simplejson
from twython import Twython
import datetime
import tweepy
import csv

#Set date and time variables for output file naming
now = datetime.datetime.now()
day =  int(now.day)
month = int(now.month)
year = int(now.year)

#OAuth information to allow remote twitter API calls
app_key='YcrhlJY6YboSWsGq8K4ZCxfa6'
app_secret='9ReXuM8lS9QKsaS48uLAwMN6a7eC1McUEWdy7onGOuXzOckT4d'
oauth_token='31175631-CxF1zlwrulH6Km6g9s6iMi8w5WmIGt4tr2fAEAFML'
oauth_token_secret='74LLjXsn0Xko3uc9ZYTj6z1FZ6lB75wvGaqdaBP25AzJG'

t = Twython(app_key, 
	app_secret,
	oauth_token,
	oauth_token_secret)

#The twitter IDs to grab data from
ids = ["realDonaldTrump", "HillaryClinton", "JebBush", "BernieSanders"]

users = t.lookup_user(screen_name = ids)

#function to get 200 tweets in user history
def get_all_tweets(tweep):
	auth = tweepy.OAuthHandler(app_key, app_secret)
	auth.set_access_token(oauth_token, oauth_token_secret)
	api = tweepy.API(auth)

	with open("%s_tweets_%i.%i.csv" %(tweep, now.month, now.day), 'a') as f:
		write = csv.writer(f)
		write.writerow(["Date Created" "Tweet Content"])

	for tweet in tweepy.Cursor(api.user_timeline, id=tweep, since="2015-6-30", until="2015-9-28").items(200):

		tweetlist = [tweet.created_at, tweet.text.encode("utf-8")]

		#write to CSV
		with open("%s_tweets_%i.%i.csv" %(tweep, now.month, now.day), 'a') as f:
			write = csv.writer(f)
			write.writerows([tweetlist])
		pass

def get_user_info(user):
	users = t.lookup_user(screen_name = ids)

	#Initialize output file with dates
	output = "TW_User_Data.%i.%i" % (now.month, now.day)

	#Data fields to include in output
	data = "UserID Screen-Name Name Followers-Count Friends-Count Statuses-Count".split()

	#Open and write to output file
	outfp = open(output, "a")
	outfp.write(string.join(data, "\t") + "\n")

	for entry in user:
		#create dictionary
		r = {}
		for f in data:
			r[f] = ""
		#Assign value of ID field from JSON output of user lookup to field in dictionary
		r['UserID'] = entry['id']
		r['Screen-Name'] = entry['screen_name']
		r['Name'] = entry['name']
		r['Followers-Count'] = entry['followers_count']
		r['Friends-Count'] = entry['friends_count']
		r['Statuses-Count'] = entry['statuses_count']
		print r

		#initialize empty list
		list = []
		for d in data:
			list.append(unicode(r[d]).replace("\/", "/"))
		outfp.write(string.join(list, "\t").encode("utf-8") + "\n")

	outfp.close()

if __name__ == '__main__':
	for entry in ids:
		print entry
		get_all_tweets(entry)
	get_user_info(users)