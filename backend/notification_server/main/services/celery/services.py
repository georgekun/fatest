"""
Здесь у нас функции, которые используются в task celery
"""

import json
import requests
from django_celery_beat.models import CrontabSchedule, PeriodicTask
from dotenv import load_dotenv

from django.conf import settings
from django.utils import timezone

from ...models import Message, Newsletter, Client

load_dotenv()


def create_messages(clients, newsletter):
    messages = []
    for client in clients:
        message, created = Message.objects.get_or_create(
                newsletter=newsletter,
                client=client
        )
        messages.append(message)
    return messages


def send_message(message: Message) -> int:
    phone = message.client.phone_number
    text = message.newsletter.message_text
    url = f"https://probe.fbrq.cloud/v1/send/{message.id}"

    body = json.dumps({
            "id": message.id,
            "phone": phone,
            "text": text
    })
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {settings.JWT_AUTH_TOKEN}"
    }

    try:
        response = requests.post(url=url, headers=headers, data=body)
        if response.status_code == 200:
            return True
        return False
    except requests.exceptions.RequestException as e:
        return False


def get_filtered_clients(**kwargs):
    id_newsletter = kwargs.get('id_newsletter', None)
    if not id_newsletter:
        return
    newsletter = Newsletter.objects.filter(id=id_newsletter).first()
    filter_by_code = newsletter.client_filter_operator_code
    filter_by_tag = newsletter.client_filter_tag

    queryset = Client.objects.all()

    if filter_by_code is not None and filter_by_code != '':
        queryset = queryset.filter(operator_code=filter_by_code)

    if filter_by_tag is not None and filter_by_tag != '':
        queryset = queryset.filter(tag=filter_by_tag)

    return queryset, newsletter


def create_task_for_mailing():

    """ при старте приложения функция создаст периодическую задачу, для отправки почты"""
    crontab, created = CrontabSchedule.objects.get_or_create(minute=0, hour=8, timezone='Europe/Moscow')
    if created:
        task = PeriodicTask.objects.get_or_create(
            name="Отправка отчета на почту",
            task='send_report_by_email',
            crontab=crontab,
            start_time=timezone.now()
        )
        return task
