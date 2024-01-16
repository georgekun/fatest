"""Здесь находятся функции,
которые работают с моделями celery,
после изменения нашей модели newsletter"""

import json
from datetime import datetime
from typing import Union
from django_celery_beat.models import ClockedSchedule, PeriodicTask

from ...models import Newsletter, TaskNewsletterAssociation


def create_connect_task(newsletter: Newsletter) -> Union[PeriodicTask, None]:
    clocked_schedule, created = ClockedSchedule.objects.get_or_create(
        clocked_time=newsletter.launch_datetime
    )
    kwargs = {"id_newsletter": newsletter.id}

    if clocked_schedule:
        task = PeriodicTask.objects.create(
            name=f"Рассылка {newsletter.id}",
            task="send_newsletter",
            kwargs=json.dumps(kwargs),
            clocked=clocked_schedule,
            start_time=newsletter.launch_datetime,
            expires=newsletter.end_datetime,
            one_off=True,
        )
        connect = TaskNewsletterAssociation.objects.create(periodic_task=task, newsletter=newsletter)
        return task


def update_connect_task(newsletter: Newsletter) -> bool:
    association = TaskNewsletterAssociation.objects.filter(newsletter=newsletter).first()
    if not association:
        return False
    task = association.periodic_task
    if not task:
        return False

    task.start_time = newsletter.launch_datetime
    task.expires = newsletter.end_datetime
    if not task.enabled and newsletter.end_datetime > datetime.now(newsletter.end_datetime.tzinfo):
        task.enabled = True
    task.save()
    clocked_schedule = task.clocked
    clocked_schedule.clocked_time = newsletter.launch_datetime
    clocked_schedule.save()
    return True


def delete_connect_task(newsletter: Newsletter) -> None:
    association = TaskNewsletterAssociation.objects.filter(newsletter=newsletter).first()
    if association:
        task = association.periodic_task
        task.delete()



