# CSV → Kafka → Faust → MongoDB

This project demonstrates streaming CSV data into Kafka, processing with Faust, and saving results into MongoDB.

## 🧱 Stack
- Kafka (via Confluent Platform)  
- MongoDB  
- Faust (Python Stream Processing)  

## 🚀 Quickstart
1. Start all services (Kafka, Zookeeper, MongoDB, Faust app, Producer) with Docker Compose:  
```bash
docker-compose up --build
