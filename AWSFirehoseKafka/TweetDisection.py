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
import cityGen
from collections import Counter
from pymongo import MongoClient
import pymongo
client = MongoClient()
db = client.test

##########################################################################
##########################################################################

#Main function to do LSA
def main(tweet):
    #Tweets = '3tweet.json'
    Tweets = tweet.message.value
    #Tweets = json.loads(string)
    #Tweets = [w.encode("utf-8") for w in Tweets]
    #print(Tweets)
    
    tweet_text, tweet_geo = TweetParser(Tweets)
    tweet_clean = corpusGen(tweet_text)
    wordCounter(tweet_clean, tweet_geo)
    
##########################################################################
##########################################################################



 
########################################################################## 
##########################################################################  

#Parses the large, horribly overinformative (for my purposes)
#json that each tweet comes with into two python lists: 
#----->   tweet_text, tweet_geo
#from these dicts I will be able to do the LSA with gensim

##########################################################################
##########################################################################

def TweetParser(Tweets):
    
    #Read in the full json for each tweet into python dicts
    tweet_json = []
    #with open(Tweets) as f:
     #    for line in f:
      #       tweet_json.append(json.loads(line))
    tweet_json.append(json.loads(Tweets))
    #for tweet in Tweets

    #Parse the json file to extract the text object and the lattitude and
    #longitude coordinates from where the tweet came from  
    tweet_text = []
    tweet_geo = []   
    for obj in tweet_json:
        tweet_text.append(obj['text'])
        tweet_geo.append(obj['coordinates']['coordinates'])
        
    return tweet_text, tweet_geo        
    
##########################################################################           
##########################################################################            



##########################################################################           
##########################################################################            
def corpusGen(tweet_text):
    st = LancasterStemmer()
    
    tweet_clean_text = []
    for doc in tweet_text:
        twitterWords = doc.split()
        
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
                      "bad", "let","stop", "well", "tell"]
    
        twitterWords = [w for w in twitterWords if not w in noiseWords]
        twitterWords = [w.encode("utf-8") for w in twitterWords]
        #twitterWords = [st.stem(w) for w in twitterWords]
        #twitterWords = ' '.join(twitterWords)
        #tweet_clean_text.append(twitterWords)
           
    return twitterWords
            
##########################################################################           
##########################################################################            



##########################################################################
##########################################################################
def wordCounter(tweet_clean, tweet_geo):
 
    city = cityGen.cityGen(tweet_geo[0][0],tweet_geo[0][1])
   
    doc2 = db.WordCount.fine_one({'city':'USA'})
    totalWords = len(doc2['data']) + 1
    doc = db.WordCount.find_one({'city': city})
    
    if doc is None:
        return
        
    wordnums = len(doc['data'])
    wordnum = str(wordnums+1)
    tweet = tweet_clean
 
    for word in tweet:
            wordnum = str(wordnums)
            if not db.WordCount.find_one({'city': 'USA', 'data.word':word}):
                db.WordCount.update({'city': city}, {'$set': {'data.'+ wordnum +'.word':word, 'data.'+ wordnum +'.count':1}})
                db.WordCount.update({'city': 'USA'}, {'$set': {'data.'+ totalWords +'.word':word, 'data.'+ totalWords +'.count':1}})
                wordnums = wordnums + 1
                totalWords = totalWords + 1
            else:
                for i in range(0, wordnums): 
                    if db.WordCount.find_one({'city': city, 'data.' + str(i) + '.word':word}):
                        db.WordCount.update({'city': city}, {'$inc': {'data.' + str(i) + '.count':1}})
                for j in range(0, totalWords):
                    if db.WordCount.find_one({'city': 'USA', 'data.' + str(j) + '.word':word}):
                        db.WordCount.update({'city': 'USA'}, {'$inc': {'data.' + str(j) + '.count':1}})
                        
                        
            
                
##########################################################################
##########################################################################


#main()
