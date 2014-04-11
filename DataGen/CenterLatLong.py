import twitter
import json
import pprint
import enchant
import csv
from geopy.geocoders import GoogleV3
#still a work in progress, just have the geo-location being put into an array

tweet_json = []

with open('SmallTweets.json') as f:
    for line in f:
        tweet_json.append(json.loads(line))

geo = []
count = 0
for obj in tweet_json:
    count = count+1
    if obj['place'] != None and obj['place']['name'] != None:
        geo.append(obj['place']['name'])


print(geo)

