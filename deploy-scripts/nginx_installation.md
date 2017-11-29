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
```worker_processes  1;
events {
    worker_connections  1024;
}
rtmp {
    server {
        listen 1935;
        chunk_size 4000;

        application live {
            live on;

            #treba nastviť cestu k streamovanému videu
            exec ffmpeg -re -i /home/matus/test2/xxx2.mp4 -async 1 -vsync -1
                        -ar 44100 -c:v libx264 -b:v 128K -b:a 128k -f flv rtmp://localhost/show/xxx2_low
			                  -ar 44100 -c:v libx264 -b:v 1024K -b:a 1024k -f flv rtmp://localhost/show/xxx2_hd;
        }

        application show {
            live on;
            hls on;

            #treba nastaviť priečinok pre hls
            hls_path /home/matus/test/hls/;

            # Instruct clients to adjust resolution according to bandwidth
            hls_variant _low BANDWIDTH=1024; # Low bitrate, sub-SD resolution
            hls_variant _hd BANDWIDTH=2048; # Source bitrate, source resolution
        }

	application mpeg {
        live on; # Allows live input

        #treba nastviť cestu k streamovanému videu
        exec ffmpeg -re -i /home/matus/test2/xxx2.mp4 -vcodec libx264 -acodec aac -f flv rtmp://localhost/dash/stream;
        }

        application dash {
            live on;
            dash on;

            #treba nastaviť priečinok pre dash
            dash_path /home/matus/test/dash/;
        }
    }
}

http {
    sendfile off;
    tcp_nopush on;
    aio on;
    directio 512;

    server {
        listen 80;

        location /hls {
            types {
                application/vnd.apple.mpegurl m3u8;
            }
            #treba nastaviť root adresár
            root /home/matus/test;
        }

	location /dash {
	    types {
                application/dash+xml mpd;
            }
            #treba nastaviť root adresár
            root /home/matus/test;
            add_header Cache-Control no-cache;
            add_header 'Access-Control-Allow-Origin' '*';
        }
    }
}
```

---
### 3. Spusti server
  sudo /usr/local/nginx/sbin/nginx

##### vypnutie servera
  sudo /usr/local/nginx/sbin/nginx -s stop
