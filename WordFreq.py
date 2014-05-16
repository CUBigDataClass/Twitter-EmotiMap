from __future__ import division
import twitter
import json
import pprint
import enchant
import csv
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import itertools
from nltk.corpus import stopwords

#loads tweets into python dicts
tweet_json = []
with open('BigTweets.json') as f:
    for line in f:
            tweet_json.append(json.loads(line))
                                            
            
#extra check to make sure each tweet english			
for obj in tweet_json:
    if obj['lang'] != "en":
        tweet_json.remove(obj)  

#parses eac h tweet for text object     
tweets = []
count = 0
for obj in tweet_json:
      count = count + 1
      tweets.append(obj['text'])  

#puts words of tweets in a nested list
tweetWords = []  
i = 0
for obj in tweet_json:
    i = i + 1
    wordlist = tweets[i-1].split()
    tweetWords.append(wordlist)

twitterWords = list(itertools.chain(*tweetWords))

#remove stop words using NLTK corpus
twitterWords = [word.lower() for word in twitterWords]
twitterWords = [w for w in twitterWords if not w in stopwords.words('english')]

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

print(twitterWords)
#Not enough stop words taken out from NLTK corpus
with open('customstopwords.csv', 'rb') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';', quotechar='"')

countsT = Counter(twitterWords)


lT = countsT.items()
lT.sort(key = lambda item: item[1])

topWords = []
k = len(lT)
for i in range(0, 28):
    topWords.append(lT[k-i-1])
    


#this graphs the word frequency
#####################################
labels, values = zip(*topWords)
indexes = np.arange(len(labels))
width = .1

plt.bar(indexes, values, width)
plt.xticks(indexes + width*.5, labels)
plt.show()
###################################

    