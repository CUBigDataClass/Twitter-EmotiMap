import twitter
import json
import pprint
import enchant


#still a work in progress, just have the geo-location being put into an array

tweet_json = []

with open('SampleMongoDb.json') as f:
    for line in f:
        tweet_json.append(json.loads(line))

geo = []
count = 0
for obj in tweet_json:
    count = count+1
    geo.append(obj['coordinates']['coordinates'])

print(geo)

