#!/usr/bin/env bash
# 
sudo apt update
sudo apt install -y nginx

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

echo "<html>
<head>
</head>
<body>
ALX
</body>
</html>" > /data/web_static/releases/test/index.html

if [ -L /data/web_static/current ]; then
    rm /data/web_static/current
fi

ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/

sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

sudo service nginx restart
