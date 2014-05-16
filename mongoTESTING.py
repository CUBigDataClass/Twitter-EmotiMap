import twitter
import json
from pymongo import MongoClient
from bson import BSON
from bson import json_util

client = MongoClient()
db = client.test
collection = db.TweetsGeo
    
for d in collection.find()[:2]:
    print(d)
    

#b = json.dumps(a, sort_keys = True, indent = 4, default = json_util.default)


    
