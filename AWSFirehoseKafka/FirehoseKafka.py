import twitter
import json
import time
import TweetDisection
import threading, logging, time
from kafka.client import KafkaClient
from kafka.consumer import SimpleConsumer
from kafka.producer import SimpleProducer

api = twitter.Api(consumer_key='DdU16WP4VM7P9PHOUJ57g', consumer_secret='s3MRayg34QV82RXOsG3VZquXY0JY7k0osL5SfKZ2o', access_token_key='419788290-Lq3CrrkXbRhv6Sdn06KDCQRueErUpXCF8dFZY2wo', access_token_secret='wcmsAk7CUrJHifaTcZiAVsN4tCC4rmV8h59rw2ZUeO3S6', cache=None)

#api = twitter.Api(consumer_key = 'G1ztnAQmyriiOqcyt9pGQ', consumer_secret='TzNhT5oCWMMU5eIk6E61bgSuXQ7qDHuYv5EbYwDKQ', access_token_key='572163554-le5J2mX0lb5IMOdAVPyAkxQ8M24UIMIyQMafqyur', access_token_secret='EB9xZBqfRVuga9tUsrqiP5qf5PHCsvsGrm3UkHz3nyZPc', cache=None)
client = KafkaClient("localhost:9092")
producer = SimpleProducer(client)
consumer = SimpleConsumer(client, "text-Tweets", "Tweets")  

class Producer(threading.Thread):
    def run(self):
        while True:
            statuses = api.GetStreamSample()
            for obj in statuses:
                if 'text' in obj and 'coordinates' in obj and 'lang' in obj and 'place' in obj:
                    place = obj['place']
                    if place != None and 'country_code' in place:
                        if obj['text'] != None and obj['coordinates'] != None and obj['place']['country_code'] == "US" and obj['lang'] == "en":
                            a = json.dumps(obj)
                            producer.send_messages('Tweets', a)
                            print('tweetsent')
                            
                        
class Consumer(threading.Thread):
    def run(self):
        while(True):
            for message in consumer:
                time.sleep(.1)
                TweetDisection.main(message)
                print('consumed')


Producer().start()
Consumer().start()
#except Exception,e:
 #   print str(e)                     
                            