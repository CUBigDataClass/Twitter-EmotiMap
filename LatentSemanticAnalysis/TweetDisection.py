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
import getCity

##########################################################################
##########################################################################

#Main function to do LSA
def main():
    Tweets = '3tweet.json'
    tweet_text, tweet_geo = TweetParser(Tweets)
    tweet_clean_text = corpusGen(tweet_text)
    for tweet in tweet_geo:
    	print getCity.getCity(tweet[0],tweet[1]) 
    print(tweet_clean_text)
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
        twitterWords = [st.stem(w) for w in twitterWords]
        twitterWords = ' '.join(twitterWords)
        #this is for tokenizing, not working yet
        #' '.join(twitterWords)
        #twitterWords = word_tokenize(twitterWords)
        tweet_clean_text.append(twitterWords)
   
	
    newTweetList = []	
    for tweet in tweet_clean_text:
	newTweetList.append(tweet.split())

    tweet_clean_text =  newTweetList

    # remove words that appear only once
    all_tokens = sum(tweet_clean_text, [])
    tokens_once = set(word for word in set(all_tokens) if all_tokens.count(word) == 1)
    tweet_clean_text = [[word for word in text if word not in tokens_once] for text in tweet_clean_text]

       
    return tweet_clean_text
            
##########################################################################           
##########################################################################            



##########################################################################
##########################################################################



main()
