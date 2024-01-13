from django.contrib import admin

from django_celery_beat.models import (
    IntervalSchedule,
    CrontabSchedule,
    SolarSchedule,
    ClockedSchedule,
    PeriodicTask,
)


from .models import Client, Newsletter, Message, Statistic

admin.site.register([Client, Newsletter, Message, Statistic])

admin.site.unregister([IntervalSchedule, CrontabSchedule, SolarSchedule, ClockedSchedule, PeriodicTask])
