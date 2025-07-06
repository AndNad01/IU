import csv
import json
from kafka import KafkaProducer
import time

# Wait for Kafka
time.sleep(60)

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

with open('app/iot_telemetry_data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        time.sleep(5)
#        row['id'] = int(row['id'])
#        row['value'] = int(row['value'])
#        "ts", "device", "co", "humidity", "light", "lpg", "motion", "smoke", "temp"
        producer.send('iot', row)
        producer.flush()
        print("Sent:", row)

#producer.flush()
