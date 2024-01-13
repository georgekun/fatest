
from celery import shared_task

from .models import Statistic
from .services.celery.services import get_filtered_clients, create_messages, send_message


@shared_task(name='send_newsletter')
def send_newsletter(**kwargs):
    clients, newsletter = get_filtered_clients(**kwargs)
    messages = create_messages(clients, newsletter)
    stats, created = Statistic.objects.get_or_create(newsletter=newsletter)

    for message in messages:
        status = send_message(message)
        message.send_status = status
        stats.count_sent_messages += 1
        if status:
            stats.count_success_sent_messages += 1
        stats.save()
        message.save()
    return True


