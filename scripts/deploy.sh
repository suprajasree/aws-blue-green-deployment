#!/bin/bash

IMAGE_NAME="bluegreen-app"
CONTAINER_NAME="green"
PORT="8082"

echo "Starting deployment..."

echo "Building Docker image..."

docker build -t $IMAGE_NAME ./app


echo "Starting Green container..."

docker rm -f $CONTAINER_NAME 2>/dev/null


docker run -d \
--name $CONTAINER_NAME \
-e ENVIRONMENT=GREEN \
-e VERSION=2.0 \
-p $PORT:5000 \
$IMAGE_NAME


echo "Waiting for application startup..."

sleep 5


echo "Running health check..."

./scripts/health-check.sh


if [ $? -ne 0 ]; then

    echo "Health check failed."
    echo "Deployment stopped."

    exit 1

fi


echo "Health check passed."


echo "Switching traffic to Green..."

./scripts/switch.sh green


if [ $? -eq 0 ]; then

    echo "Deployment completed successfully."

else

    echo "Traffic switch failed."
    ./scripts/rollback.sh
    exit 1

fi
