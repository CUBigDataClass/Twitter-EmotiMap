from pymongo import MongoClient
from operator import itemgetter

client = MongoClient()
db = client.test.WordCount2

data = db.find_one()

#for keys in data:
#	print keys, len(data[keys])

wordList = []
for words in data["Los Angeles"]:
	wordList.append([words, data["Los Angeles"][words]])

print sorted(wordList, key=itemgetter(1))


