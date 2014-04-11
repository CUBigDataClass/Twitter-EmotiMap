from __future__ import division
import twitter
import json
import pprint
import enchant
import csv



tweet_json = []
with open('BigTweets.json') as f:
    for line in f:
            tweet_json.append(json.loads(line))

#clean up the sample so non US tweets do not get through
print(len(tweet_json))
for obj in tweet_json:
    if obj['lang'] != "en":
        tweet_json.remove(obj)  


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

print(words)

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



N = len(geo)
newPerclit = []
newGeo = []
for count in range(0,N-1):
    #print(fuck)
    #print(count)
    newTag = 0
    if geo[count][1] > 49.345786:
        newTag = 1
    elif geo[count][1] < 24.7433195:
        newTag = 1
    elif geo[count][0] > -66.9513812:
       newTag = 1
    elif geo[count][0] < -124.794409:
       newTag = 1
    if newTag != 1:
        newGeo.append(geo[count])
        newPerclit.append(spellCount[count])
print(len(geo))
print(len(newGeo))
print(len(newPerclit))
 

with open("LatLong.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(newGeo)
    
with open("PercentLit.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(newPerclit)

