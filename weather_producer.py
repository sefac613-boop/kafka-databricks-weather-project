import requests
import json
import time
from kafka import KafkaProducer

# Ayarların zaten doğru, bunları koruyoruz
API_KEY = "2814d11e550f45e9928161155261405" 
CITY = "Amsterdam"
TOPIC = "weather_reports"

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def fetch_and_send():
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}&aqi=no"
    try:
        response = requests.get(url)
        res_data = response.json()
        
        # Görev listesindeki (Task 5) verileri ayıklıyoruz
        data = {
            "City": res_data['location']['name'],
            "Temperature": res_data['current']['temp_c'],
            "Humidity": res_data['current']['humidity'],
            "Wind_speed": res_data['current']['wind_kph'],
            "Local_time": res_data['location']['localtime'],
            "Last_updated": res_data['current']['last_updated']
        }
        
        producer.send(TOPIC, data)
        print(f"Veri gönderildi: {data['City']} - {data['Temperature']}°C")
    except Exception as e:
        print(f"Hata: {e}")

if __name__ == "__main__":
    while True:
        fetch_and_send()
        # Görev gereği 60 saniye bekliyoruz
        time.sleep(60)