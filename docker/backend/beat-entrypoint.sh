#!/bin/sh

until cd /app/backend
do
    echo "Waiting for server volume..."
done

celery -A backend beat -l INFO