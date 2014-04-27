import getCity
import twitter
import json
import enchant
import csv
import nltk as nk
import gensim as gsm
from gensim import corpora, models, similarities
import numpy as np
import nltk as nltk
import itertools
from nltk.stem.lancaster import LancasterStemmer
from nltk import word_tokenize
from nltk.corpus import stopwords
from pymongo import MongoClient

client = MongoClient()
db = client.test

def MongoToJson():
	Json = db.WordCount2.find_one()
	return Json


def TweetParser(Tweets):

    #Read in the full json for each tweet into python dicts
    tweet_json = []
    with open(Tweets) as f:
        for line in f:
            tweet_json.append(json.loads(line))

    #Parse the json file to extract the text object and the lattitude and
    #longitude coordinates from where the tweet came from  
    tweet_text = []
    tweet_geo = []
    for obj in tweet_json:
        tweet_text.append(obj['text'])
        tweet_geo.append(obj['coordinates']['coordinates'])

    return tweet_text, tweet_geo

def tweetTokenizer(tweet_text):
	st = LancasterStemmer()	
	twitterWords = tweet_text.split()

        	#remove stop words using NLTK corpus
       	twitterWords = [word.lower() for word in twitterWords]
       	twitterWords = [w for w in twitterWords if not w in stopwords.words('english')]

        	#remove custom list of stop words using experimentation
       	noiseWords = ["i'm", "like", "get", "don't", "it's", "go", "lol", "got",
                      "one", "know", "@", "good", "want", "can't", "need", "see",
                      "people", "going", "back", "really", "u", "think", "right",
                      "never", "day", "time", "never", "that's", "even", ",", "."
                      "make", "wanna", "you're", "come", "-", "still", "much", "someone",
                      "today", "gonna", "new", "would", "take", "always", "im", "i'll",
                      "best", "'", "feel", "getting", "say", "tonight", "last", "ever",
                      "better", "i've", "look", "fucking", "way", "could", "!", "oh"
                      "tomorrow", "night", "first", "miss", "ain't", "thank", "2", "bad"
                      "little", "thanks", "something", "wait", "&amp;", "`", "oh", "make",
                      "bad", "let","stop", "well", "tell", " "]

       #	twitterWords = [w for w in twitterWords if not w in noiseWords]
       #	twitterWords = [st.stem(w) for w in twitterWords]
	twitterWords = [''.join(ch for ch in w if ch.isalnum()) for w in twitterWords]

	return twitterWords

def processWordCount(tweet_text,tweet_geo):
	wordList = tweetTokenizer(tweet_text)	
	city =  getCity.getCity(tweet_geo[0],tweet_geo[1])
	print city, tweet_geo[1], tweet_geo[0]
	json1_data = MongoToJson()
	for word in wordList:
		if city not in json1_data:
			json1_data[city] = {}
		if word not in json1_data[city].keys():
			json1_data[city][word] = 0
	
		json1_data[city][word] += 1
	#db.WordCount.remove()
	db.WordCount2.update({},json1_data)
	
testJson = '''

{
	"Los Angeles":{
		"fuck":10,	
		"ass":40,
		"shit":500
	},
        "Denver":{
         	"fuck":100,      
                "ass":50,
               	"shit":22500      
        }
}

''' 


#testTweet = '3tweet.json'
#tweet_text, tweet_geo = TweetParser(testTweet)
#processWordCount(tweet_text[0],tweet_geo[0])


