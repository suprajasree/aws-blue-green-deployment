#!/bin/bash

GREEN_URL="http://localhost:8082/health"
BLUE_URL="http://localhost:8081/health"

echo "Checking Blue environment..."

curl -f $BLUE_URL

if [ $? -eq 0 ]; then
    echo "Blue is healthy"
else
    echo "Blue health check failed"
fi


echo ""
echo "Checking Green environment..."

curl -f $GREEN_URL

if [ $? -eq 0 ]; then
    echo "Green is healthy"
else
    echo "Green health check failed"
    exit 1
fi
