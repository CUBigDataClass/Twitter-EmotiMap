import twitter
import json
import pprint
import enchant
import csv
import cityGen

tweet_json = []

with open('BigTweets.json') as f:
    for line in f:
        tweet_json.append(json.loads(line))

geo = []
for obj in tweet_json:
    geo.append(obj['coordinates']['coordinates'])
    
for coord in geo:
    
    if cityGen.cityGen(coord[0], coord[1]) == 'New York':
        print('fuck ya""')
    



