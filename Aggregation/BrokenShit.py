import twitter
import json
import time
import TweetDisection
import threading, logging, time
from kafka.client import KafkaClient
from kafka.consumer import SimpleConsumer
from kafka.producer import SimpleProducer

api = twitter.Api(consumer_key = 'G1ztnAQmyriiOqcyt9pGQ', consumer_secret='TzNhT5oCWMMU5eIk6E61bgSuXQ7qDHuYv5EbYwDKQ', access_token_key='572163554-le5J2mX0lb5IMOdAVPyAkxQ8M24UIMIyQMafqyur', access_token_secret='EB9xZBqfRVuga9tUsrqiP5qf5PHCsvsGrm3UkHz3nyZPc', cache=None)

class Producer(threading.Thread):
   # daemon = True
    print('hi')
    def run(self):
        print('hi')
        client = KafkaClient("localhost:9092")
        producer = SimpleProducer(client, batch_send = True, batch_send_every_n = 20, batch_send_every_t = 60)
        while True:
            statuses = api.GetStreamSample()
            for obj in statuses:
                if 'text' in obj and 'coordinates' in obj and 'lang' in obj and 'place' in obj:
                    place = obj['place']
                    if place != None and 'country_code' in place:
                        if obj['text'] != None and obj['coordinates'] != None and obj['place']['country_code'] == "US" and obj['lang'] == "en":
                            a = json.dumps(obj)
                            
                            producer.send_messages('Tweets', a)
                            

class Consumer(threading.Thread):
    #daemon = True
    
    def run(self):
       # print('hi')
        client = KafkaClient("localhost:9092")
        consumer = SimpleConsumer(client, "text-Tweets", "Tweets")  
        while(True):
            for message in consumer:
                TweetDisection.main(message)
            
def main():
    threads = [
        Producer(),
        #Consumer()
    ]
    
    for t in threads:
        t.start()
    #threading.Timer(10, main).start()
    time.sleep(5)
  
main()  
#if __name__ == "main":
#    logging.basicConfig(
#        format = '%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d',
#        level = logging.DEBUG
#    )                

#main()
                            
                            
                            
