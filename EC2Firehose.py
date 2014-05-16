#!/usr/bin/python

import twitter
import json
from kafka.client import KafkaClient
from kafka.consumer import SimpleConsumer
from kafka.producer import SimpleProducer


client = KafkaClient("localhost:9092")
producer = SimpleProducer(client)
consumer = SimpleConsumer(client, "text-Tweets", "my-topic")

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
					print('hi')
					continue
			
#print json.dumps(s)
