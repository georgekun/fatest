#!/bin/sh

until cd /app/notification_server
do
    echo "Waiting for server volume..."
done


# run a worker :)
celery -A notification_server worker  -l INFO
