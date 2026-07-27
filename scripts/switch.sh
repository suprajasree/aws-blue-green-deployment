#!/bin/bash

ENVIRONMENT=$1

NGINX_CONFIG="/etc/nginx/sites-available/blue-green"

if [ -z "$ENVIRONMENT" ]; then
    echo "Usage: ./switch.sh blue|green"
    exit 1
fi


if [ "$ENVIRONMENT" == "blue" ]; then

    echo "Switching traffic to BLUE..."

    sudo sed -i 's|proxy_pass http://127.0.0.1:8082;|proxy_pass http://127.0.0.1:8081;|' $NGINX_CONFIG


elif [ "$ENVIRONMENT" == "green" ]; then

    echo "Switching traffic to GREEN..."

    sudo sed -i 's|proxy_pass http://127.0.0.1:8081;|proxy_pass http://127.0.0.1:8082;|' $NGINX_CONFIG


else

    echo "Invalid environment"
    echo "Use blue or green"
    exit 1

fi


sudo nginx -t

if [ $? -eq 0 ]; then

    sudo systemctl reload nginx

    echo "Traffic switched successfully to $ENVIRONMENT"

else

    echo "Nginx configuration failed"
    exit 1

fi
