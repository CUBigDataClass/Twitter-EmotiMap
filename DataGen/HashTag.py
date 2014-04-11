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

print(len(tweets))

#creates dict of hashtags
hashEntity = []
coord = []
for obj in tweet_json:
    hashEntity.append(obj["entities"]["hashtags"])
    coord.append(obj['coordinates']['coordinates'])


Indiv_hashtags = []
hashtaglist = []
N = len(hashEntity)
for i in range(0, N):
    single = []
    if hashEntity[i] != []:
        j = -1
        for obj in hashEntity[i]:
            j = j+1
            single.append(hashEntity[i][j]['text'])
            hashtaglist.append(hashEntity[i][j]['text'])
    Indiv_hashtags.append(single)

counts = Counter(hashtaglist)

print(len(hashtaglist))

l = counts.items()
l.sort(key = lambda item: item[1])

topTags = []
k = len(l)
for i in range(0, 28):
    topTags.append(l[k-i-1])
    
#this graphs the hashtag frequency
#####################################
labels, values = zip(*topTags)
indexes = np.arange(len(labels))
width = 1

plt.bar(indexes, values, width)
plt.xticks(indexes + width*.5, labels)
plt.show()
#########################################



