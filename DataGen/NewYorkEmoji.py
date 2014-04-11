from __future__ import division
import twitter
import json
import pprint
import enchant
import csv
from collections import Counter
import matplotlib.pyplot as plt
import numpy as n
import math as m
import itertools



#loads tweets into python dicts
tweet_json = []
with open('BigTweets.json') as f:
    for line in f:
            tweet_json.append(json.loads(line))
                                            
            
#extra check to make sure each tweet english			
for obj in tweet_json:
    if obj['lang'] != "en":
        tweet_json.remove(obj)  

geo = []
count = 0
for obj in tweet_json:
    count = count+1
    geo.append(obj['coordinates']['coordinates'])


####################################################
#Check if tweet is within Colorado Bubble
count = 0
lo1 = m.radians(-73.94)
la1 = m.radians(40.67)
tweetWords = []
for obj in tweet_json:
    count = count + 1
    
    #Get coordinates of tweet
    lo2 = m.radians(geo[count-1][0])
    la2 = m.radians(geo[count-1][1])
    
    #Calculate the distance away from Colorado center
    dlon = abs(lo1-lo2)
    dlat = abs(la1-la2)
    a = (m.sin(dlat/2)**2) + (m.cos(la1)*m.cos(la2)*(m.sin(dlon/2)**2))
    c = 2*m.atan2(m.sqrt(a), m.sqrt(1-a))
    d = 3961*c
    
    #Check if distance between points is too great
    if d < 100:
        tweetWords.append(obj['text'].split())
        
print(tweetWords)
print(d)
print(geo[0][0])
print(geo[0][1])    
print(len(tweetWords))


twitterWords = list(itertools.chain(*tweetWords))

    

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
indexes = n.arange(len(labels))
width = .1

fig = plt.figure()
plt.bar(indexes, values, width)
plt.xticks(indexes + width*.5, labels)
plt.show()
#fig.savefig('emoji.png', dpi = fig.dpi)

###################################
