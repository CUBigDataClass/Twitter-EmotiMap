import twitter
import json
import enchant
import csv
import nltk as nk
import gensim as gsm
import numpy as np
import nltk as nltk
import itertools
from nltk.stem.lancaster import LancasterStemmer
from nltk import word_tokenize

##########################################################################
##########################################################################

#Main function to do LSA
def main():
    Tweets = '3tweet.json'
    tweet_text, tweet_geo = TweetParser(Tweets)
    tweet_clean_text = DocumentCleaner(tweet_text)
    
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

#Tokenizes and de-Stems the documents of each tweet for better analysis

##########################################################################
##########################################################################
def DocumentCleaner(tweet_text):
    st = LancasterStemmer()
    count = 0
    for doc in tweet_text:
        count = count + 1
        text = tweet_text[count-1]
        tok_text = word_tokenize(text)
        tweet_text[count-1] = tok_text
        word_num = 0
        for word in tok_text:
            word_num = word_num + 1
            tweet_text[count-1][word_num-1] = st.stem(tweet_text[count-1][word_num-1])
    
    return tweet_text  
##########################################################################
##########################################################################  

main()