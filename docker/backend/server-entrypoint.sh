#!/bin/sh

until cd /app/notification_server
do
    echo "Waiting for server volume..."
done


until python manage.py migrate
do
    echo "Waiting for the database to be ready..."
    sleep 2
done

python manage.py collectstatic --noinput
gunicorn notification_server.wsgi --bind 0.0.0.0:8000 --workers 4 --threads 4
