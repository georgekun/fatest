from django.contrib import admin

from django_celery_beat.models import (
    IntervalSchedule,
    SolarSchedule,
    ClockedSchedule,
    PeriodicTask,
    CrontabSchedule
)


from .models import Client, Newsletter, Message, Statistic

admin.site.register([Client, Newsletter, Message, Statistic])
admin.site.unregister([IntervalSchedule, SolarSchedule,CrontabSchedule, ClockedSchedule, PeriodicTask])
