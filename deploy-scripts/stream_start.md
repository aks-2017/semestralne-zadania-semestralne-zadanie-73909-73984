# Spustenie MPEG-DASH streamu

### 1. Nastav IP adresy serva a klienta

### 2. Choď do priečinka s videom a spusti príkaz

ffmpeg -re -i 480i.ts -vcodec libx264 -vprofile baseline -g 30 -acodec aac -strict -2 -f flv rtmp://localhost/dash/stream

### 3. Otvor VLC a pripoj sa na adresu
  http://IP_adresa_servera:8080/dash/stream.mpd
