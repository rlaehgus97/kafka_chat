# 채팅 시스템
# Producer 채팅 보내는 애

from kafka import KafkaProducer
import json
import time

p = KafkaProducer(
        # 보내고 싶은 서버
        bootstrap_servers=['localhost:9092'],
        # json 형태의 값을 암호화
        value_serializer=lambda x:json.dumps(x).encode('utf-8')
)

print("채팅 프로그램 - 메시지 발신자")
print("메시지를 입력하세요. (종료시 'exit' 입력)")

# 입력값 원할때까지 받기
while True:
    msg = input("YOU: ")
    if msg.lower() == 'exit':   #.lower exit대소문자 다 받기
        break

    # json 형태
    data = {'message': msg, 'time': time.time()}
    # producer로 보내기
    p.send('chat', value=data)
    p.flush()
    time.sleep(0.1)
