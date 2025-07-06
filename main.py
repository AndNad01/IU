import faust
from pymongo import MongoClient
import time
import os

# Wait for Kafka and Mongo to be ready
time.sleep(30)

# Connect to Mongo
mongo_uri = os.getenv("MONGO_URI", "mongodb://mongo:27017")
mongo = MongoClient(mongo_uri)
db = mongo["streaming"]
collection = db["iot"]

# Connect to Kafka
kafka_broker = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "kafka:9092")
app = faust.App('faust-app', broker=f'kafka://{kafka_broker}')

# Define message schema
class Message(faust.Record, serializer='json'):
    ts: str
    device: str
    co: str
    humidity: str
    light: str
    lpg: str
    motion: str
    smoke: str
    temp: str

# Declare topic
topic = app.topic('iot', value_type=Message)

# Faust agent
@app.agent(topic)
async def process(stream):
    async for msg in stream:
        print(f"Processing: msg={msg}")
        collection.insert_one({"id": msg.ts, "value": msg})

# Start the Faust app
#if __name__ == '__main__':
# Do not call app.main(); Faust will be started via CLI
#    app.main()
