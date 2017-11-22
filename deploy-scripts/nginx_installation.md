# Návod na inštaláciu a konfiguráciu HTTP servera nginx s rtmp modulom (Ubuntu)
### 1. Stiahni a nainštaluj
sudo apt-get install build-essential libpcre3 libpcre3-dev libssl-dev

sudo wget http://nginx.org/download/nginx-1.12.0.tar.gz
sudo tar xzf nginx-1.12.0.tar.gz
cd nginx-1.12.0

sudo ./configure --with-http_ssl_module --add-module=../nginx-rtmp-module
sudo make
sudo make install

### 2. Upravo konfiguračný súbor nginx
sudo gedit /usr/local/nginx/conf/nginx.conf

---
worker_processes 1;
events {
&nbsp;worker_connections 1024;
}
rtmp {
&nbsp;server {
&nbsp;&nbsp;listen 1935;
&nbsp;&nbsp;chunk_size 4000;
&nbsp;&nbsp;application dash {
&nbsp;&nbsp;&nbsp;live on;
&nbsp;&nbsp;&nbsp;dash on;
     # nastav priecinok dash_path
&nbsp;&nbsp;&nbsp;dash_path /home/matus/test/dash;
&nbsp;&nbsp}
&nbsp;}
}
http {
&nbsp;server {
&nbsp;&nbsp;listen 8080;
&nbsp;&nbsp;types {
&nbsp;&nbsp;&nbsp;application/dash+xml mpd;
&nbsp;&nbsp;&nbsp;application/vnd.apple.mpegurl m3u8;
&nbsp;&nbsp;&nbsp;video/mp2t ts;
&nbsp;&nbsp;}
&nbsp;&nbsp;location /dash {
    # nastav root priecinok
&nbsp;&nbsp;&nbsp;root /home/matus/test;
&nbsp;&nbsp;&nbsp;add_header Cache-Control no-cache;
&nbsp;&nbsp;}
&nbsp;}
}
---
### 3. Spusti server
  sudo /usr/local/nginx/sbin/nginx

##### vypnutie servera
  sudo /usr/local/nginx/sbin/nginx -s stop
