#!/usr/bin/python

import twitter
import json
from pymongo import MongoClient
client = MongoClient()
db = client.test


#this is Dillon Fancher's API key
api = twitter.Api(consumer_key='G1ztnAQmyriiOqcyt9pGQ', consumer_secret='TzNhT5oCWMMU5eIk6E61bgSuXQ7qDHuYv5EbYwDKQ', access_token_key='572163554-le5J2mX0lb5IMOdAVPyAkxQ8M24UIMIyQMafqyur', access_token_secret='EB9xZBqfRVuga9tUsrqiP5qf5PHCsvsGrm3UkHz3nyZPc', cache=None)

while(True):
	statuses = api.GetStreamSample()
	
	#Iterate through all geolocated tweets
	for obj in statuses:
		if 'text' in obj and 'coordinates' in obj and 'lang' in obj and 'place' in obj:
			place = obj['place']
			if 	place != None and 'country_code' in place:
				if obj['text'] != None and obj['coordinates'] != None and obj['place']['country_code'] == "US" and obj['lang'] == "en":
					# Grab the user who created the tweet
					#print "Username: %s" % (obj['user']['name'])
					# Record the tweet
					#print "Tweet: %s\nLocation: (%f, %f)\n" % (obj['text'], obj['coordinates']['coordinates'][0], obj['coordinates']['coordinates'][1])
					db.TweetsGeo.update({'id' : obj['id']}, obj, True)
					continue
			
#print json.dumps(s)
