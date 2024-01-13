
from django.db import models
from django_celery_beat.models import PeriodicTask
from django.utils import timezone


class Newsletter(models.Model):
    id = models.AutoField(primary_key=True)
    launch_datetime = models.DateTimeField(default=timezone.now)
    message_text = models.TextField(max_length=500)
    client_filter_operator_code = models.CharField(max_length=10, null=True, blank=True)
    client_filter_tag = models.CharField(max_length=255, null=True, blank=True)
    end_datetime = models.DateTimeField()

    def __str__(self):
        return f"Id: {self.id}    Message: {self.message_text}"


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    phone_number = models.CharField(max_length=12, unique=True)
    operator_code = models.CharField(max_length=10)
    tag = models.CharField(max_length=255)
    timezone = models.CharField(max_length=255)


class Message(models.Model):
    id = models.AutoField(primary_key=True)
    creation_datetime = models.DateTimeField(default=timezone.now)
    send_status = models.BooleanField(default=False)
    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)


class Statistic(models.Model):
    id = models.AutoField(primary_key=True)
    creation_datetime = models.DateTimeField(default=timezone.now)
    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE)
    count_sent_messages = models.IntegerField(default=0)
    count_success_sent_messages = models.IntegerField(default=0)


class TaskNewsletterAssociation(models.Model):
    periodic_task = models.ForeignKey(PeriodicTask, on_delete=models.CASCADE)
    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE)

    def __str__(self):
        return f"Link - Task: {self.periodic_task}, Newsletter: {self.newsletter}"
