#!/usr/bin/python

import twitter
import json
from pymongo import MongoClient
client = MongoClient()
db = client.test

api = twitter.Api(consumer_key='DdU16WP4VM7P9PHOUJ57g', consumer_secret='s3MRayg34QV82RXOsG3VZquXY0JY7k0osL5SfKZ2o', access_token_key='419788290-Lq3CrrkXbRhv6Sdn06KDCQRueErUpXCF8dFZY2wo', access_token_secret='wcmsAk7CUrJHifaTcZiAVsN4tCC4rmV8h59rw2ZUeO3S6', cache=None)

while(True)
	statuses = api.GetStreamSample()
	
	#Iterate through all geolocated tweets
	for obj in statuses:
		if 'text' in obj and 'coordinates' in obj and 'lang' in obj and 'place' in obj:
			place = obj['place']
			if 	place != None and 'country_code' in place:
				if obj['text'] != None and obj['coordinates'] != None and obj['place']['country_code'] == "US" and obj['lang'] == "en":
					# Grab the user who created the tweet
					print "Username: %s" % (obj['user']['name'])
					# Record the tweet
					print "Tweet: %s\nLocation: (%f, %f)\n" % (obj['text'], obj['coordinates']['coordinates'][0], obj['coordinates']['coordinates'][1])
					db.TweetsGeo.update({'id' : obj['id']}, obj, True)
	
					continue
			
#print json.dumps(s)
