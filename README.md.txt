# ISO 50001 Chatbot 

Bu proje ISO 50001 Enerji Yönetim Sistemi hakkında temel sorulara cevap veren bir chatbot uygulamasıdır.  
Proje Rasa Framework ve Docker kullanılarak geliştirilmiştir.  

#Özellikler
- ISO 50001 hakkında scope, requirements, benefits sorularını cevaplar.
- Basit bir web arayüzü üzerinden kullanıcı ile sohbet imkanı sunar.
- Rasa NLU + Rules tabanlıdır.
- Docker Compose ile kolayca çalıştırılabilir.

#Proje Yapısı
iso50001-chatbot/
rasa/ # Rasa chatbot dosyaları
nlu.yml # Kullanıcı örnek cümleleri (intents)
rules.yml # Kurallar
domain.yml # Botun cevapları
config.yml # NLP ayarları
actions/ # Özel Python aksiyonları
web/ # Basit web arayüzü
index.html
docker-compose.yml # Servisleri çalıştıran dosya

#Kurulum ve Çalıştırma
#1.Gereksinimler
- [Docker Desktop](https://www.docker.com/products/docker-desktop) kurulu olmalı.

#2.Çalıştırma
Terminalde proje klasörüne git:
```bash
cd iso50001-chatbot
docker-compose up
3.Kullanım
Bot API’si → http://localhost:5005
Web arayüzü → http://localhost:8080

Örnek Sorular
"hello"
"What does ISO 50001 cover?"
"What are the requirements of ISO 50001?"
"What are the benefits of ISO 50001?"

Kullanılan Teknolojiler
Python 3.9
Rasa 3.6
Rasa SDK 3.6
Docker & Docker Compose