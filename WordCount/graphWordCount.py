from pymongo import MongoClient
from operator import itemgetter
import numpy as np
import matplotlib.pyplot as plt


client = MongoClient()
db = client.test.WordCount

data = db.find_one()

#for keys in data:
#       print keys, len(data[keys])

wordList = []
for city in data.keys():
    for words in data[city]:
        wordList.append([words, data[city][words]])
    wordList = sorted(wordList, key=itemgetter(1), reverse=True)
        
            
    N = 20
    ind = np.arange(N)  # the x locations for the groups
    width = 0.35       # the width of the bars
    fig, ax = plt.subplots()
    rects1 = ax.bar(ind, [x[1] for x in wordList[1:21]] , color='r')
    # add some
    ax.set_ylabel('Count')
    ax.set_title(city + " Top 20 words (stemmed)")
    ax.set_xticks(ind+width)
    ax.set_xticklabels( [str(x[0]) for x in wordList[1:21]] )
    fig.set_size_inches(18.5,10.5)
    fig.savefig(city+"_stemmed")
        
    wordList = []
        
