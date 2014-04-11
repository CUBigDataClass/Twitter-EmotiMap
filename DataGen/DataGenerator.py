from __future__ import division
import twitter
import json
import enchant
import csv
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import math as m
import itertools
from nltk.corpus import stopwords
import subprocess

#Main Function to pass arguments from PHP
###########################################################################
def main(graphID, location):
    #Sanity Check
    print('hello world')
    
    #Turn .json into a python Dict
    tweet_json = []
    with open('BigTweets.json') as f:
        for line in f:
                tweet_json.append(json.loads(line))
           
    #put geolocation of each tweet into a list     
    geo = []
    for obj in tweet_json: 
        geo.append(obj['coordinates']['coordinates'])
    
    #Get bubble's lattitude, longitude center for counting based on location
    if location == 'US':
        specific = 0
    elif location == 'Denver':
        specific = 1
        lat1 = 39.73
        lon1 = -104.98
        dMax = 57.56
        zoom = 6
    elif location == 'NYC':
        specific = 1
        lat1 = 40.67
        lon1 = -73.94
        dMax = 30.0
        zoom = 9
    elif location == 'NewOrleans':
        specific = 1
        lat1 = 29.9667
        lon1 = -90.05
        dMax = 28.0
        zoom = 9
    elif location == 'Oakland':
        specific = 1
        lat1 = 37.8044
        lon1 = -122.2708
        dMax = 30.0
        zoom = 11
    elif location == 'Detroit':
        specific = 1
        lat1 = 42.3314
        lon1 = -83.0458
        dMax = 30.0
        zoom = 9
    elif location == 'LaPaloma':
        specific == 1
        lat1 = 26.0486
        lon1 = -97.6669
        dMax = 30.0
        zoom = 13
    else:
        print('Sorry, we do not have this City yet, plese try again.')
    
    #Parses each tweet for text object for the specified location   
    tweets = []
    tweetWords = []
    geoSpecific = []
    count = 0
    
    #Limit counts to a specified bubble
    if specific == 1:
        print('We are not in the US')
        for obj in tweet_json:
            count = count+1
            d = LatLongDist(lat1, lon1, geo[count-1][1], geo[count-1][0])
            if d <= dMax:
                tweets.append(obj['text'])
                tweetWords.append(obj['text'].split())
                geoSpecific.append(obj['coordinates']['coordinates'])
    
    #Do the counts on all of the United States
    elif specific == 0:
        geoSpecific = geo
        for obj in tweet_json:
            count = count+1
            tweets.append(obj['text'])
            tweetWords.append(obj['text'].split())
    
    if graphID == 'HashTagFreq':
        HashTagFrequency(tweet_json, tweets)
    elif graphID == 'WordFreq':
        WordFrequency(tweet_json, tweetWords)
    elif graphID == 'EmojiFreq':
        EmojiFrequency(tweetWords)
    elif graphID == 'PercLit':
        PercentLiteracy(tweets, geoSpecific, zoom, lat1, lon1, dMax)
    else:
        print('Sorry we do not have this Visualization yet, please try again.')
    #HashTagFrequency(tweet_json, tweets)
    #WordFrequency(tweet_json, tweetWords)
    #d = LatLongDist(39.0, -105.5, 38.0, -104.5, tweet_json)
    #PercentLiteracy(tweets, tweet_json, geo):
    
###########################################################################



###
#All of the functions to return the data to display on the WebUI are below
###
###########################################################################    
def HashTagFrequency(tweet_json, tweets):
    #Takes 'entity' attribute 'hashtags' from each Tweet
    hashEntity = []
    for obj in tweet_json:
        hashEntity.append(obj["entities"]["hashtags"])
    
    #Splits 'hashtags' into seperate items of a list
    Indiv_hashtags = []
    hashtaglist = []
    N = len(hashEntity)
    for i in range(0, N):
        single = []
        if hashEntity[i] != []:
            j = -1
            for obj in hashEntity[i]:
                j = j+1
                if hashEntity[i][j]['text'] != 'Job' and hashEntity[i][j]['text'] != 'Jobs':
                    hashtaglist.append(hashEntity[i][j]['text'])
        
    #Count the number of occurences of each tweet
    counts = Counter(hashtaglist)  

    #Create list of the items in our individual hashtag list 
    #to sort by frequency
    l = counts.items()
    l.sort(key = lambda item: item[1]) 
    
    #Create a shortened list of the highest frequency hashtags
    topTags = []
    k = len(l)
    for i in range(0, 10):
        topTags.append(l[k-i-1])
    
    #this graphs the hashtag frequency
    #####################################
    labels, values = zip(*topTags)
    indexes = np.arange(len(labels))
    width = 1
    
    fig = plt.figure()
    plt.bar(indexes, values, width)
    plt.xticks(indexes + width*.5, labels)
    plt.show()
    fig.savefig('HashFreq.png', dpi = 300)
    #########################################
###########################################################################



###########################################################################
def WordFrequency(tweet_json, tweetWords):
    #Flatten the list of tweet words
    twitterWords = list(itertools.chain(*tweetWords))

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

    #Count number of occurences of each hashtag
    countsT = Counter(twitterWords)

    #Create structure to sort the list of counts by frequency
    lT = countsT.items()
    lT.sort(key = lambda item: item[1])

    topWords = []
    k = len(lT)
    for i in range(0, 10):
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
    fig.savefig('WordFreq.png', dpi = 300)
    ###################################
###########################################################################

###########################################################################
def EmojiFrequency(tweetWords):
    #Flatten List of words
    twitterWords = list(itertools.chain(*tweetWords))
    
    #Filter out everything but Emoji's
    Emoji = []
    N = len(twitterWords)
    for i in range(0, N):
        if (repr(twitterWords[i][:2]) == repr(twitterWords[i][:3])) \
        and len(repr(twitterWords[i][:2])) == 13:
            Emoji.append(twitterWords[i])

    #Count the frequency of each Emoji
    countsT = Counter(Emoji)

    #Sort the frequency
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
    fig.savefig('emoji.png', dpi = 300)
    ###################################
###########################################################################



###########################################################################
def PercentLiteracy(tweets, geo, zoom, lat1, lon1, dMax):
    
    tweetWords = []
    for obj in tweets:
        tweetWords.append([])
        
    spellCount = []
    i = 0
    if(len(tweets)) == 0:
        print('No tweets in this location')
        return 0;
    for obj in tweets:
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
        spellCount.append(litCount)
    
    N = len(tweets)
    newPerclit = []
    newGeo = []
    for count in range(0,N-1):
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
   
    percent = round(sum(spellCount)/len(spellCount),2)
    print(percent)
    
    zoom = zoom
    lat = lat1
    lon = lon1
    Rargs = []
    Rargs.append([1])
    Rargs.append([percent])
    Rargs.append([zoom])
    Rargs.append([lat])
    Rargs.append([lon])
    Rargs.append([dMax])
    
    with open("PercentLit.csv", "wb") as f:
        writer = csv.writer(f)
        writer.writerows(Rargs)

    retcode = subprocess.call(['Rscript', 'PercentLiteracyMAP.R'])
###########################################################################



###########################################################################
def LatLongDist(lat1, lon1, lat2, lon2):
   
        
        #Convert latitude and longitude into radians
        la1 = m.radians(lat1)
        la2 = m.radians(lat2)
        lo1 = m.radians(lon1)
        lo2 = m.radians(lon2)
       
        #Calculate the distance between [lat1, long1] and [lat2, long2]
        dlon = abs(lo1-lo2)
        dlat = abs(la1-la2)
        a = (m.sin(dlat/2)**2) + (m.cos(la1)*m.cos(la2)*(m.sin(dlon/2)**2))
        c = 2*m.atan2(m.sqrt(a), m.sqrt(1-a))
        d = 3961*c
    
        return(d)
###########################################################################
  

main('PercLit', 'Denver')





