from django.contrib import admin

from .models import Client, Newsletter, Message, Statistics

admin.site.register([Client, Newsletter, Message, Statistics])
