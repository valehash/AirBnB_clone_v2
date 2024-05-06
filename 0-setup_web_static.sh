#!/usr/bin/env bash
#Script to  set up the web servers for web static deployment

#Install Nginx if it does not exist
if ! command -v nginx &> /dev/null; then
    sudo apt-get update
    sudo apt-get install -y nginx
fi

#  make the directories web_static/realeases/test and webstaic/shared
sudo mkdir -p /data/web_static/{releases/test,shared}
# changing the owner and group of the data foder to ubuntu
sudo chown -R ubuntu:ubuntu /data/
 
#symlink web_static/current with web_static/realeases/test
if [ -L /data/web_static/current ]; then rm -Rf /data/web_static/current ; fi
# if [ -d "$WORKING_DIR" ]; then rm -Rf $WORKING_DIR; fi
sudo ln -sf /data/web_static/releases/test /data/web_static/current
echo "<html>
<head>
</head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee "/data/web_static/current/index.html" &> /dev/null


sudo sed -i '44i\ location /hbnb_static {\
            alias /data/web_static/current/;\}' /etc/nginx/sites-available/default
