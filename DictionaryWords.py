from __future__ import division
import twitter
import json
import pprint
import enchant
import csv


#Temporarily import json from the sample Andrew posted from the MongoDB, future of #how to filter/process files has yet to been decided.
tweet_json = []
with open('BIGsampleUS.json') as f:
    for line in f:
        tweet_json.append(json.loads(line))
     
#Look at each tweet, extract its 'text' object, parse each 'text' object into it's #respective word list for analyzation of each word in the tweet   
tweets = []
count = 0
for obj in tweet_json:
    count = count + 1
    tweets.append(obj['text'])

#Initialize a list of lists to avoid error: "list index out of range"
tweetWords = []
for obj in tweet_json:
    tweetWords.append([])

##############################
#######enchant syntax#########
#syntax to use enchant to check for dictionary compatibility    
    #d = enchant.Dict("en_US")
    #a = d.check("hi")
    #print(a)
#############################
##############################
#Go through each 'text' object and parse it into a list of words for each tweet

    
words = []
count = 0
for obj in tweet_json:
    count = count+1
    words.append(obj['text'])
    
wordlist = []
spellCount = []
i = 0
for obj in tweet_json:
    i = i + 1
    wordlist = tweets[i-1].split()
    for w in range(0, len(wordlist)-1):
        wordlist[w] = wordlist[w].replace("\\", "NAYSAY")
    literacy = []
    for j in range(0, len(wordlist)-1):
        d = enchant.Dict("en_US")
        a = d.check(wordlist[j])
        literacy.append(a)
    N = len(wordlist)
    trueCount = 0
    falseCount = 0
    for k in range (0, N-1):
        if literacy[k] != False:
            tweetWords[i-1].append(wordlist[k])
            trueCount = trueCount + 1
        else:
            falseCount = falseCount + 1
  
    litCount = trueCount/N
    spellCount.append([litCount])


geo = []
count = 0
for obj in tweet_json:
    count = count+1
    geo.append(obj['coordinates']['coordinates'])


with open("LatLong.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(geo)
    
with open("PercentLit.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(spellCount)

