#!/usr/bin/env bash
#Script to  set up the web servers for web static deployment

if ! command -v nginx &> /dev/null; then
    sudo apt-get update
    sudo apt-get install -y nginx
fi

sudo mkdir -p -m=755 /data/web_static/{releases/test,shared}||exit 0
echo "Holberton" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/

sudo sed -i '44i\ location /hbnb_static {\
            alias /data/web_static/current/;\}' /etc/nginx/sites-available/default

sudo service nginx restart
exit 0
