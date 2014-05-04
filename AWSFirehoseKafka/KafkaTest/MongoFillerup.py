from pymongo import MongoClient
import TweetDisection 

client = MongoClient()
db = client.test

Data = db.TweetsGeo.find()
dictData = TweetDisection.MongoToDict()

timer = 0

for tweet in Data:
    	tweet_text = tweet['text']
	tweet_clean = TweetDisection.corpusGen(tweet_text)
	TweetDisection.wordCounter(dictData,tweet_clean, tweet['geo']['coordinates'])
	if timer%100 == 0:
		print timer
	timer +=1
