"""Здесь вспомогательные функции для отправки отчета на почту"""
import os

import magic
import pyexcel

from django.conf import settings
from django.core.mail import EmailMessage

from ...models import Newsletter


def send_email_with_attachment(subject, message, from_email, recipient_list, attachment_path):
    with open(attachment_path, 'rb') as file:
        file_content = file.read()

    mime_type = magic.from_buffer(file_content, mime=True)
    file_name = os.path.basename(attachment_path)

    email = EmailMessage(subject, message, from_email, recipient_list)
    email.attach(file_name, file_content, mime_type)

    # Send the email
    return email.send()


def create_report_file(filename: str = "file"):

    data = [['id', 'launch datetime',
            'message text', 'operator code',
             'tag', 'end datetime']]

    for n in Newsletter.objects.all():
        row = [
            n.id,
            n.launch_datetime if n.launch_datetime else 'N/A',
            n.message_text if n.message_text else 'N/A',
            n.client_filter_operator_code if n.client_filter_operator_code else 'N/A',
            n.client_filter_tag if n.client_filter_tag else 'N/A',
            n.end_datetime if n.end_datetime else 'N/A',
        ]
        data.append(row)

    file_path = os.path.join(settings.BASE_DIR, 'media', f'{filename}.xls')
    book = pyexcel.Sheet(data)
    book.save_as(file_path)
    return file_path

