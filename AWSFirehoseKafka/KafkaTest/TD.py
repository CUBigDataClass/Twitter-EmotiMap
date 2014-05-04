import twitter
import json
import nltk as nk
import nltk as nltk
from nltk.stem.lancaster import LancasterStemmer
from nltk import word_tokenize
from nltk.corpus import stopwords
import getCity
from pymongo import MongoClient
import pymongo

client = MongoClient()
db = client.test

##########################################################################
##########################################################################

#Main function to do LSA
def main(dictData, tweet):
    Tweets = tweet.message.value
  
    #we need to define this more globally so we dont have to load the DB into a dict every time a tweet comes in 
    #dictData = MongoToDict()        
    tweet_text, tweet_geo = TweetParser(Tweets)
    tweet_clean = corpusGen(tweet_text)
    wordCounter(dictData, tweet_clean, tweet_geo)
    
##########################################################################
##########################################################################



##########################################################################
##########################################################################

def TweetParser(Tweets):
    
    tweet_json = []
    tweet_json.append(json.loads(Tweets))

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
    
    for doc in tweet_text:
        twitterWords = doc.split()        
    
        #remove stop words using NLTK corpus
        twitterWords = [word.lower() for word in twitterWords]
        twitterWords = [w for w in twitterWords if not w in stopwords.words('english')]
        #twitterWords = [w for w in twitterWords if repr(w[:2]) != repr(w[:3])]
        twitterWords = [w for w in twitterWords if w[:1] != '@' and w[:1] != '#' and w[:4] != 'http']
       
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
        twitterWords = [w for w in twitterWords if repr(w[:2]) != repr(w[:3])]
        twitterWords = [w for w in twitterWords if w[:1] != '@' and w[:1] != '#' and w[:4] != 'http']
        twitterWords = [w for w in twitterWords if repr(w).find('\\') == -1]
        twitterWords = [w.rstrip('.') for w in twitterWords]
        twitterWords = [w.rstrip('!') for w in twitterWords]
        twitterWords = [w.rstrip('?') for w in twitterWords]
          
 
    return twitterWords
            
##########################################################################           
##########################################################################            

def MongoToDict():
        wordDict = {}
	Json = db.WordCount.find()
	for x in Json:
                city = x['city']
                for y in x['data']:
                        if city not in wordDict:
                                wordDict[city] = {}
                        if y is not None:
                                if y['word'] is not None:
                                        wordDict[city][y['word']] = y['count']

        return wordDict


##########################################################################
##########################################################################

def wordCounter(dictData, tweet_clean, tweet_geo):
        city = getCity.getCity(tweet_geo[0][1],tweet_geo[0][0])
        for word in tweet_clean:
                if city not in dictData:
                        dictData[city] = {}
                if word not in dictData[city].keys():
                        dictData[city][word] = 0
             #   if 'USA' not in dictData:
              #          dictData['USA'] = 0
              #  if word not in dictData['USA'].keys():
               #         dictData['USA'][word] = 0

                dictData[city][word] += 1
        #        if city != 'USA':
         #               dictData['USA'][word] += 1

                doc = db.WordCount.find_one({'city': city})


		if doc == None:
			return

                wordnums = len(doc['data'])
                wordnum = str(wordnums+1)


#                if db.WordCount.find_one({"city":"USA","data.word":word}):
 #                       db.WordCount.update({"city":"USA","data.word":word},{'$set':{'data.$.word':word, 'data.$.count':dictData['USA'][word]}},True)
 #               else:
  #                      db.WordCount.update({"city":"USA","data.word":{'$exists':True}},{'$set':{'data.' + wordnum + '.word':word, 'data.' + wordnum + '.count':dictData['USA'][word]}})

                if db.WordCount.find_one({"city":city,"data.word":word}):
                        db.WordCount.update({"city":city,"data.word":word},{'$set':{'data.$.word':word, 'data.$.count':dictData[city][word]}},True)
                else:
                        db.WordCount.update({"city":city,"data.word":{'$exists':True}},{'$set':{'data.' + wordnum + '.word':word, 'data.' + wordnum + '.count':1}})
                       
                        
            
                
##########################################################################
##########################################################################


#main()
