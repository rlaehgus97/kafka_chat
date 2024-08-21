from kafka import KafkaProducer
import time
import json

producer = KafkaProducer(
        bootstrap_servers=['localhost:9092'],
        value_serializer=lambda x:json.dumps(x).encode('utf-8') 
)

start = time.time()

for i in range(10):
    data = {'str': 'value' + str(i)}
    producer.send('topic1', value=data)
    producer.flush()

end = time.time() #measure proceed time
print("[DONE]:", end-start)

