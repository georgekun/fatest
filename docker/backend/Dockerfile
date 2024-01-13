FROM python:3.10

WORKDIR /app
# RUN apt-get update && apt-get install -y supervisor

RUN pip install --upgrade pip
RUN pip install gunicorn
ADD ./requirements.txt /app/
RUN pip install -r requirements.txt

ADD ./backend/notification_server /app/notification_server
ADD ./docker /app/docker

RUN mkdir -p /app/logs
RUN chmod +x /app/docker/backend/server-entrypoint.sh
RUN chmod +x /app/docker/backend/worker-entrypoint.sh
RUN chmod +x /app/docker/backend/beat-entrypoint.sh
