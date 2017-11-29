# Spustenie MPEG-DASH streamu

### 1. Nastav IP adresy servera a klienta

### 2. Choď do priečinka s videom a spusti príkaz

#### HLS
ffmpeg -re -i xxx2.mp4 -vcodec libx264 -acodec aac -f flv rtmp://localhost/live
#### DASH
ffmpeg -re -i xxx2.mp4 -vcodec libx264 -acodec aac -f flv rtmp://localhost/dash/stream

### 3. Otvor VLC a pripoj sa na adresu
#### DASH
  http://IP_adresa_servera/dash/stream.mpd
#### HLS
  http://IP_adresa_servera/hls/xxx2.m3u8
