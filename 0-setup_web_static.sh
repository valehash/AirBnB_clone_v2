#!/usr/bin/env bash
#Script to  set up the web servers for web static deployment

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
echo "Holberton" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/

sudo sed -i '44i\ location /hbnb_static {\
            alias /data/web_static/current/;\}' /etc/nginx/sites-available/default

sudo service nginx restart
