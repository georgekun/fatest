#!/bin/sh

until cd /app/notification_server
do
    echo "Waiting for server volume..."
done

celery -A notification_server beat -l INFO