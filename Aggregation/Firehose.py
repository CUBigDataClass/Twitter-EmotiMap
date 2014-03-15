#!/usr/bin/python

import twitter
import json
import pprint

# Andrew's API Credentials
#api = twitter.Api(consumer_key='kt3lmNFHN6p7MVfc0PMg',consumer_secret='3JvBprZAawaXJoGpqequIeBMJx5ibZW7Wqc6FquoILU', access_token_key='58371709-WbrfIEF0EVONTkaxiboYcTGOy5arWKtAd4MDbBQkK', access_token_secret='nAQdXoWYryK3LvlM3Nztj6doj1ciU9MOWLdLqdN0MWPgJ',cache=None)

# Matt's API Credentials for alternate use
api = twitter.Api(consumer_key='DdU16WP4VM7P9PHOUJ57g', consumer_secret='s3MRayg34QV82RXOsG3VZquXY0JY7k0osL5SfKZ2o', access_token_key='419788290-Lq3CrrkXbRhv6Sdn06KDCQRueErUpXCF8dFZY2wo', access_token_secret='wcmsAk7CUrJHifaTcZiAVsN4tCC4rmV8h59rw2ZUeO3S6', cache=None)


statuses = api.GetStreamSample()

# Prints a single tweet's JSON inline - useful for analyzing structure of a tweet
#pp = pprint.PrettyPrinter(indent=4)
#for obj in statuses:
#	if 'text' in obj and obj['text'] != None and 'lang' in obj and obj['lang'] == 'en' and obj['entities']['hashtags'] != None:
#		print pp.pprint(obj)
#		break

#Iterate through all geolocated tweets
for obj in statuses:
	if 'text' in obj and 'coordinates' in obj and 'lang' in obj:
		if obj['text'] != None and obj['coordinates'] != None and obj['lang'] == "en":
			coordinates = obj['coordinates']['coordinates']
			print "Tweet: %s\nLocation: (%f, %f)" % (obj['text'], coordinates[0], coordinates[1])
			# If the place is named, list it
			if 'place' in obj and obj['place'] != None:
				print "Place: %s" % obj['place']['full_name']
			continue