# kafka-databricks-weather-project

Live weather analysis and average temperature tracking using real-time streaming.

## 📌 Project Overview

This project collects live weather data from Amsterdam using the WeatherAPI, streams it through Apache Kafka, and processes it with Apache Spark on Databricks. The Kafka broker running locally is exposed to the internet via an ngrok tunnel, allowing Databricks to consume the stream remotely.

## 🏗️ Architecture

WeatherAPI → Python Producer → Kafka (Docker) → ngrok Tunnel → Databricks Spark → Delta Lake


## 🛠️ Technologies Used

- **WeatherAPI** – Real-time weather data source (Amsterdam)
- **Python** – Kafka producer script
- **Apache Kafka** – Message broker (via Docker)
- **Zookeeper** – Kafka coordination
- **Docker & Docker Compose** – Local infrastructure
- **ngrok** – TCP tunnel to expose local Kafka to Databricks
- **Apache Spark (Databricks)** – Stream processing and aggregation
- **Delta Lake** – Output storage on Databricks
- **Kafka UI** – Local monitoring at `http://localhost:8081`

## 🚀 How to Run

### 1. Start Kafka
```bash
docker-compose up -d
```

### 2. Start ngrok tunnel on port 9093
```bash
ngrok tcp 9093
```
Copy the ngrok address and update `EXTERNAL://` in `docker-compose.yml`, then restart Docker.

### 3. Run the Producer
```bash
python weather_producer.py
```
Weather data will be sent to the `weather_reports` Kafka topic every 60 seconds.

### 4. Monitor Messages
Open Kafka UI at `http://localhost:8081` to monitor live messages.

### 5. Run Databricks Notebook
Update `kafka_server` in the notebook with your current ngrok address and run the notebook to process and store data in Delta Lake.

## 📊 Output

The processed data includes:
- City
- Average Temperature (°C)
- Average Humidity (%)
- Average Wind Speed (km/h)

## ⚠️ Notes

- The ngrok address changes every restart. Update `docker-compose.yml` and the Databricks notebook accordingly.
- Never commit your `.env` file — it contains API keys.
