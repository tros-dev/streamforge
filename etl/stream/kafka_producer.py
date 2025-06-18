from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

def send_data():
    for i in range(10):
        data = {'record': i}
        producer.send('stream_data', value=data)
        print(f"Sent: {data}")
        time.sleep(1)

if __name__ == '__main__':
    send_data()
