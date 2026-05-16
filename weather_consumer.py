from kafka import KafkaConsumer
import json

# Kafka Consumer Ayarları
consumer = KafkaConsumer(
    'weather_reports',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest', # En baştan itibaren tüm verileri oku
    enable_auto_commit=True,
    group_id='wind-speed-monitor', # Bu tüketici grubunun adı
    value_deserializer=lambda x: json.loads(x.decode('utf-8')) # Gelen paketi aç
)

print("🌀 Rüzgar Hızı Takibi Başlatıldı... (Durdurmak için Command+C)")

try:
    for message in consumer:
        # Kafka'dan gelen veriyi al
        data = message.value
        
        # Görev: Sadece rüzgar hızını ve şehri yazdır
        city = data.get('City', 'Bilinmiyor')
        wind_speed = data.get('Wind_speed', 0)
        local_time = data.get('Local_time', '-')

        print(f"[{local_time}] {city} - Anlık Rüzgar Hızı: {wind_speed} km/h")
        
except KeyboardInterrupt:
    print("\nTakip durduruldu.")