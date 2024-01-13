from django.contrib import admin

from .models import Client, Newsletter, Message, Statistic

admin.site.register([Client, Newsletter, Message, Statistic])
