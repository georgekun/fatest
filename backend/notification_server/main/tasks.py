
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone

from celery import shared_task

from .models import Statistic
from .services.celery.services import get_filtered_clients, create_messages, send_message
from .services.mailing.utils import create_report_file, send_email_with_attachment


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


@shared_task(name='send_report_by_email')
def send_report_by_email() -> None:
    file_path = create_report_file(f'file_{timezone.now()}')
    admin_users = User.objects.filter(is_staff=True, is_superuser=True)
    to_email = list(admin_users.values_list('email', flat=True))

    return send_email_with_attachment(
            subject="Report",
            message="Отчет по рассылкам находятся в этом файле\n",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=to_email,
            attachment_path=file_path
        )

