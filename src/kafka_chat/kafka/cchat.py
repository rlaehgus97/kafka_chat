# Consumer 채팅 받는 애

from kafka import KafkaConsumer
from json import loads
from datetime import datetime

consumer = KafkaConsumer(
        'chat', # 토픽
        bootstrap_servers=['localhost:9092'], # 받는 서버
        auto_offset_reset='earliest', # 종료중에 들어온 값도 받기
        enable_auto_commit=True,
        group_id='chat-group', # 그룹 할당
        value_deserializer=lambda x: loads(x.decode('utf-8'))
)

print("채팅 프로그램 - 메시지 수신")
print("메시지 대기중 ...")

try:
    for m in consumer: # 받은값 한줄씩 실행
        data = m.value # 값
        formatted_time = datetime.fromtimestamp(data['time']).strftime("%Y-%m-%d %H:%M:%S")
        #print(f"[FRIEND] {data['message']}, [{datetime.fromtimestamp(data['time'])}]")
        print(f"[FRIEND] {data['message']} [{formatted_time}]")
except KeyboardInterrupt:
    print("채팅 종료")
finally:
    consumer.close()
