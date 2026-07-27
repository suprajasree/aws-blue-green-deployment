#!/bin/bash

NGINX_CONFIG="/etc/nginx/sites-available/blue-green"

echo "Starting rollback..."

sudo sed -i 's|proxy_pass http://127.0.0.1:8082;|proxy_pass http://127.0.0.1:8081;|' $NGINX_CONFIG


echo "Testing Nginx configuration..."

sudo nginx -t

if [ $? -eq 0 ]; then

    sudo systemctl reload nginx

    echo "Rollback completed successfully."
    echo "Traffic is now pointing to BLUE."

else

    echo "Rollback failed. Nginx configuration error."
    exit 1

fi
