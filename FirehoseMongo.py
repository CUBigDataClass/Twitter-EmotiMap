#!/usr/bin/python

import twitter
import json
from pymongo import MongoClient
client = MongoClient()
db = client.test

api = twitter.Api(consumer_key='DdU16WP4VM7P9PHOUJ57g', consumer_secret='s3MRayg34QV82RXOsG3VZquXY0JY7k0osL5SfKZ2o', access_token_key='419788290-Lq3CrrkXbRhv6Sdn06KDCQRueErUpXCF8dFZY2wo', access_token_secret='wcmsAk7CUrJHifaTcZiAVsN4tCC4rmV8h59rw2ZUeO3S6', cache=None)


statuses = api.GetStreamSample()

#Iterate through all geolocated tweets
for obj in statuses:
	if 'text' in obj and 'coordinates' in obj and 'lang' in obj and 'country_code' in obj:
		if obj['text'] != None and obj['coordinates'] != None and obj['place']['country_code'] == "US" and obj['lang'] == "en":
			db.TweetsGeo.insert(obj)
			continue
			
#print json.dumps(s)