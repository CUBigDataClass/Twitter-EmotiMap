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

#Entire US
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


#puts words of tweets in a nested list
tweetWords = []  
i = 0
for obj in tweet_json:
    i = i + 1
    wordlist = tweets[i-1].split()
    tweetWords.append(wordlist)

twitterWords = list(itertools.chain(*tweetWords))

    
print(twitterWords)
Emoji = []
N = len(twitterWords)
for i in range(0, N):
    if (repr(twitterWords[i][:2]) == repr(twitterWords[i][:3])) and len(repr(twitterWords[i][:2])) == 13:
        Emoji.append(twitterWords[i])

   

print(len(Emoji))

countsT = Counter(Emoji)


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

fig = plt.figure()
plt.bar(indexes, values, width)
plt.xticks(indexes + width*.5, labels)
plt.show()
fig.savefig('emoji.png', dpi = fig.dpi)

###################################








