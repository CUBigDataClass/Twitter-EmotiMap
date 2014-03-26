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

#parses each tweet for text object     
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

print(twitterWords)
#Not enough stop words taken out from NLTK corpus
with open('customstopwords.csv', 'rb') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';', quotechar='"')

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


l = counts.items()
l.sort(key = lambda item: item[1])

topTags = []
k = len(l)
for i in range(0, 2):
    topTags.append(l[k-i-1])
    
#this graphs the hashtag frequency
#####################################
#labels, values = zip(*topTags)
#indexes = np.arange(len(labels))
#width = 1

#plt.bar(indexes, values, width)
#plt.xticks(indexes + width*.5, labels)
#plt.show()
#########################################


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

    
