
from rest_framework import generics
from rest_framework.response import Response

from .models import Client, Newsletter, Message
from .serializers import ClientShowSerializer, ClientSerializer
from .serializers import NewsletterSerializer, NewsletterListSerializer
from .serializers import MessageListSerializer

from .services.views.services import delete_connect_task


class ClientListView(generics.ListAPIView):
    # список всех клиентов
    queryset = Client.objects.all()
    serializer_class = ClientShowSerializer


class ClientCreateView(generics.CreateAPIView):
    # добавления нового клиента в справочник со всеми его атрибутами
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientUpdateView(generics.UpdateAPIView):
    # обновления данных атрибутов клиента
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field = 'id'


class ClientDeleteView(generics.DestroyAPIView):
    # удаления клиента из справочника
    queryset = Client.objects.all()
    lookup_field = 'id'
    

class NewsletterListView(generics.ListAPIView):
    # получения общей статистики по созданным рассылкам и количеству отправленных сообщений по ним
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterListSerializer


class NewsletterCreateView(generics.CreateAPIView):
    # добавления новой рассылки со всеми её атрибутами
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer


class NewsletterUpdateView(generics.UpdateAPIView):
    # обновления атрибутов рассылки
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer
    lookup_field = 'id'


class NewsletterDeleteView(generics.DestroyAPIView):
    # удаления рассылки
    queryset = Newsletter
    lookup_field = 'id'

    def perform_destroy(self, instance):
        delete_connect_task(instance)
        instance.delete()


class MessageListView(generics.ListAPIView):
    # получения детальной статистики отправленных сообщений по конкретной рассылке
    queryset = Message.objects.all()
    serializer_class = MessageListSerializer
    lookup_field = 'id'

    def list(self, request, *args, **kwargs):
        newsletter_id = self.kwargs.get(self.lookup_field)
        queryset = self.filter_queryset(self.get_queryset().filter(newsletter=newsletter_id))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


