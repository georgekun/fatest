
from django.db import models
from django.utils import timezone

# Сущность "рассылка" имеет атрибуты:
# уникальный id рассылки
# дата и время запуска рассылки
# текст сообщения для доставки клиенту
# фильтр свойств клиентов, на которых должна быть произведена рассылка (код мобильного оператора, тег)
# дата и время окончания рассылки: если по каким-то причинам не успели разослать все сообщения -
# никакие сообщения клиентам после этого времени доставляться не должны


class Newsletter(models.Model):
    id = models.AutoField(primary_key=True)
    launch_datetime = models.DateTimeField(default=timezone.now)
    message_text = models.TextField(max_length=500)
    client_filter_operator_code = models.CharField(max_length=10, null=True, blank=True)
    client_filter_tag = models.CharField(max_length=255, null=True, blank=True)
    end_datetime = models.DateTimeField()

    def __str__(self):
        return f"id = {self.id}    start = {self.launch_datetime}   end = {self.end_datetime}"

# Сущность "клиент" имеет атрибуты:
# уникальный id клиента
# номер телефона клиента в формате 7XXXXXXXXXX (X - цифра от 0 до 9)
# код мобильного оператора
# тег (произвольная метка)
# часовой пояс


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    phone_number = models.CharField(max_length=12)  
    operator_code = models.CharField(max_length=10)
    tag = models.CharField(max_length=255)
    timezone = models.CharField(max_length=255)

# Сущность "сообщение" имеет атрибуты:
# уникальный id сообщения
# дата и время создания (отправки)
# статус отправки
# id рассылки, в рамках которой было отправлено сообщение
# id клиента, которому отправили


class Message(models.Model):
    id = models.AutoField(primary_key=True)
    creation_datetime = models.DateTimeField(default=timezone.now)
    send_status = models.BooleanField(default=False)
    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)


class Statistics(models.Model):
    id = models.AutoField(primary_key=True)
    creation_datetime = models.DateTimeField(default=timezone.now)
    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE)
    count_sent_messages = models.IntegerField(default=0)
    count_success_sent_messages = models.IntegerField(default=0)

