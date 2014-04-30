import twitter
import json
import pprint
import enchant
import csv
import city

tweet_json = []

with open('SmallTweets.json') as f:
    for line in f:
        tweet_json.append(json.loads(line))

geo = []
for obj in tweet_json:
    geo.append(obj['coordinates']['coordinates'])
    
for coord in geo:
    print(city.cityGen(coord[0], coord[1]))
    



