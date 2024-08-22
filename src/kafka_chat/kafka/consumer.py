from kafka import KafkaConsumer, TopicPartition
from json import loads
import os

OFFSET_FILE = 'consumer_offset.txt'

def save_offset(offset):
    with open(OFFSET_FILE, 'w') as file:
        file.write(str(offset))

def read_offset():
    if os.path.exists(OFFSET_FILE):
        with open(OFFSET_FILE, 'r') as file:
            return int(file.read().strip())
    return None

saved_offset = read_offset()

consumer = KafkaConsumer(
        #"topic1",
        bootstrap_servers=['ec2-43-201-83-4.ap-northeast-2.compute.amazonaws.com:9092'],
        value_deserializer=lambda x: loads(x.decode('utf-8')),
        consumer_timeout_ms=5000,
        #auto_offset_reset='earliest', # 'earliest'이미 있던 데이터 포함  'latest'나중에 온거
        #auto_offset_reset='latest', # 'earliest', 'latest'
        #auto_offset_reset='earliest' if saved_offset is None else 'none',
        #auto_offset_reset='earliest' if read_offset(OFFSET_FILE) is None else 'none',
        group_id="tving",
        enable_auto_commit=False,
)

print('[Start] get consumer')

#saved_offset = read_offset(OFFSET_FILE)

p = TopicPartition('topic1', 0)
consumer.assign([p])

if saved_offset is not None:
    consumer.seek(p, saved_offset)
else:
    consumer.seek_to_beginning(p) # 저장된 오프셋이 없으면 처음부터 읽기

for msg in consumer:
    #print(msg)
    #print(f"topic={msg.topic}, partition={msg.partition}, offset={msg.offset}")
    print(f"offset={msg.offset}, value={msg.value}")
    save_offset(msg.offset + 1)

print('[End] get consumer')
