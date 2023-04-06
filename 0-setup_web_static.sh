#!/usr/bin/env bash
# sets up web server for deploying web_static

sudo apt-get update
sudo apt-get install -y nginx

sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "Welcome To My Test Page" /data/web_static/releases/test/index.html
sudo rm -f /data/web_static/current && ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
location_block='\tlocation /hbnb_static/ {\n\talias /data/web_static/current/;\n\t}'
sudo sed -i "/^\s*server\s*{/,/^\s*}/ s|^\s*}$|\n$location_block\n}|" /etc/nginx/sites-available/default
sudo service nginx start
