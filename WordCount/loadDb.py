import getCity
import processWordCount
from pymongo import MongoClient
import json
import itertools

client = MongoClient()
tweetDb = client.test.TweetsGeo
wordsDb = client.test.WordCount

tweets = tweetDb.find()

for tweet in tweets:
	processWordCount.processWordCount( tweet["text"],tweet["geo"]["coordinates"])
