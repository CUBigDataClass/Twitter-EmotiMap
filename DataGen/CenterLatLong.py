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
  
COgeo = []
count = -1  
for coord in geo:
    count = count+1
    if cityGen.cityGen(coord[0], coord[1]) == 'Denver':
        COgeo.append(geo[count])

print(COgeo[10])
print(COgeo[17])
print(COgeo[56])
print(COgeo[108])
        
with open("colorado.csv","wb") as f:
    writer = csv.writer(f)
    writer.writerows(COgeo)
    



