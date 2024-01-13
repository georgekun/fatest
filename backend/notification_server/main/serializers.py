
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import Client, Message, Newsletter, Statistic


class ClientShowSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'phone_number', 'tag']


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        exclude = ['id']


class NewsletterSerializer(ModelSerializer):
    class Meta:
        model = Newsletter
        fields = "__all__"


class NewsletterListSerializer(ModelSerializer):
    count_sent_messages = SerializerMethodField()
    count_success_sent_messages = SerializerMethodField()

    class Meta:
        model = Newsletter
        fields = "__all__"

    def get_count_sent_messages(self, instance):
        stats = Statistic.objects.filter(newsletter=instance).first()
        if stats:
            return stats.count_sent_messages


    def get_count_success_sent_messages(self, instance):
        stats = Statistic.objects.filter(newsletter=instance).first()
        if stats:
            return stats.count_success_sent_messages


class MessageListSerializer(ModelSerializer):
    client_number_phone = SerializerMethodField()
    message_text = SerializerMethodField()
    class Meta:
        model = Message
        fields = "__all__"

    def get_client_number_phone(self, instance):
        client = instance.client
        if client:
            return client.phone_number

    def get_message_text(self, instance):
        newsletter = instance.newsletter
        if newsletter:
            return newsletter.message_text