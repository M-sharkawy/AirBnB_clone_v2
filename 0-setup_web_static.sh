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

NGINX_CONFIG="/etc/nginx/sites-available/default"
sudo sed -i '/location \/hbnb_static {/,+2d' $NGINX_CONFIG  # Remove old config if exists
sudo bash -c "cat >> $NGINX_CONFIG" <<EOF
location /hbnb_static {
    alias /data/web_static/current;
    index index.html;
}
EOF

sudo systemctl restart nginx
