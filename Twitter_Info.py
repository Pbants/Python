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

#Set date and time variables for output file naming
now = datetime.datetime.now()
day =  int(now.day)
month = int(now.month)
year = int(now.year)

#OAuth information to allow remote twitter API calls
t = Twython(app_key='YcrhlJY6YboSWsGq8K4ZCxfa6', 
	app_secret='9ReXuM8lS9QKsaS48uLAwMN6a7eC1McUEWdy7onGOuXzOckT4d',
	oauth_token='31175631-CxF1zlwrulH6Km6g9s6iMi8w5WmIGt4tr2fAEAFML',
	oauth_token_secret='74LLjXsn0Xko3uc9ZYTj6z1FZ6lB75wvGaqdaBP25AzJG')

#The twitter IDs to grab data from
ids = "pbants, tee_tuhm, sj_mcconnell"

users = t.lookup_user(screen_name = ids)

#Initialize output file with dates
output = "TW_User_Data.%i.%i" % (now.month, now.day)

#Data fields to include in output
data = "id screen_name name followers_count friends_count".split()

#Open and write to output file
outfp = open(output, "w")
outfp.write(string.join(data, "\t") + "\n")

for entry in users:
	#create dictionary
	r = {}
	for f in data:
		r[f] = ""
	#Assign value of ID field from JSON output of user lookup to field in dictionary
	r['id'] = entry['id']
	r['screen_name'] = entry['screen_name']
	r['followers_count'] = entry['followers_count']
	r['friends_count'] = entry['friends_count']
	print r

	#initialize empty list
	list = []
	for d in data:
		list.append(unicode(r[d]).replace("\/", "/"))
	outfp.write(string.join(list, "\t").encode("utf-8") + "\n")

outfp.close()
