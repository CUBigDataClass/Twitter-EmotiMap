#!/usr/bin/python

import twitter
import json
from pymongo import MongoClient
client = MongoClient()
db = client.test

api = twitter.Api(consumer_key='kt3lmNFHN6p7MVfc0PMg',consumer_secret='3JvBprZAawaXJoGpqequIeBMJx5ibZW7Wqc6FquoILU', access_token_key='58371709-WbrfIEF0EVONTkaxiboYcTGOy5arWKtAd4MDbBQkK', access_token_secret='nAQdXoWYryK3LvlM3Nztj6doj1ciU9MOWLdLqdN0MWPgJ',cache=None)


statuses = api.GetStreamSample()
for s in statuses:
	if 'text' in s and 'geo' in s:
		if s['geo'] !=None:
			print s['text'], s['geo']
			post = s
			db.TweetsGeo.insert(post)
			continue
			
#print json.dumps(s)
