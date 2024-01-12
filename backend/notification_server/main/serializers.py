
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import Client, Message, Newsletter, Statistics


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

    def get_count_sent_messages(self, obj):
        stats = Statistics.objects.filter(newsletter=obj).first()
        return stats.count_sent_messages

    def get_count_success_sent_messages(self, obj):
        stats = Statistics.objects.filter(newsletter=obj).first()
        stats = 1/0
        return stats.count_success_sent_messages


class MessageListSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"

