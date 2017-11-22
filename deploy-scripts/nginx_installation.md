Návod na inštaláciu a konfiguráciu HTTP servera nginx s rtmp modulom (Ubuntu)

1. Stiahni a nainštaluj
  sudo apt-get install build-essential libpcre3 libpcre3-dev libssl-dev

  sudo wget http://nginx.org/download/nginx-1.12.0.tar.gz
  sudo tar xzf nginx-1.12.0.tar.gz
  cd nginx-1.12.0

  sudo ./configure --with-http_ssl_module --add-module=../nginx-rtmp-module
  sudo make
  sudo make install

2. Upravo konfiguračný súbor nginx
  sudo gedit /usr/local/nginx/conf/nginx.conf

  worker_processes 1;

  events {
    worker_connections 1024;
  }

  rtmp {
    server {
      listen 1935;
      chunk_size 4000;
      application dash {
         live on;
         dash on;
         dash_path /home/matus/test/dash;
     }
    }
  }
  # HTTP can be used for accessing RTMP stats
  http {
     server {
       listen 8080;
       types {
           application/dash+xml mpd;
           application/vnd.apple.mpegurl m3u8;
           video/mp2t ts;
       }
       location /dash {
           # Serve DASH fragments
           root /home/matus/test;
           add_header Cache-Control no-cache;
       }
     }
  }

3. Spusti server
  sudo /usr/local/nginx/sbin/nginx

  vypnutie servera
  sudo /usr/local/nginx/sbin/nginx -s stop
