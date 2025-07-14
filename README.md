# 📡 CSV → Kafka (topic: iot) → Faust → MongoDB Streaming Pipeline

This project demonstrates a real-time streaming pipeline that ingests IoT sensor data from a CSV file, streams it into **Kafka** under topic `iot`, processes it using **Faust**, and stores it in **MongoDB**.

---

## 🧱 Tech Stack

| Component   | Purpose                             |
|------------|--------------------------------------|
| Kafka      | Stream ingestion and pub/sub buffer  |
| Faust      | Stream processor in Python           |
| MongoDB    | NoSQL storage for processed data     |
| Docker     | Container orchestration              |

---

## 🔁 Data Flow

```text
[CSV File] 
   ↓
[csv_kafka_producer.py (Kafka Producer)] 
   ↓
[Kafka Topic: iot] 
   ↓
[Faust Stream Processor (main.py)] 
   ↓
[MongoDB: streaming.iot collection]

📂 File Breakdown
iot_telemetry_data.csv – Input CSV file with IoT sensor readings
csv_kafka_producer.py – Reads the CSV and sends each row as a message to Kafka topic iot
main.py – Faust app that consumes data from Kafka and stores it in MongoDB
docker-compose.yml – Starts Kafka, Zookeeper, and MongoDB containers
requirements.txt – Python dependencies

🚀 Quickstart
1. Clone the repository
git clone https://github.com/AndNad01/IU.git
cd IU

2. Install Python dependencies
pip install -r requirements.txt

3. Start Kafka, Zookeeper, MongoDB; stream CSV data to Kafka topic iot and start Faust stream processor
docker-compose up --build


🧪 Input Format: data.csv
Each row contains a snapshot of sensor readings from a device.
ts,device,co,humidity,light,lpg,motion,smoke,temp
1.5945120943859746E9,b8:27:eb:bf:9d:51,0.0049,51.0,false,0.0076,false,0.0204,22.7
Field	    Type	  Description
ts	    float	  Unix timestamp (seconds)
device  string	Device MAC address
co	    float	  Carbon monoxide level
humidity	float	  Humidity %
light	   bool	  Light detected (true/false)
lpg	     float	  LPG gas level
motion  bool	  Motion detected (true/false)
smoke    float	  Smoke level
temp	    float	  Temperature in Celsius

🔍 View Output in MongoDB
docker exec -it mongo mongosh
use streaming
db.iot.find().pretty()

🧼 Cleanup
docker-compose down -v
