
from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import Newsletter
from .services.celery.services import create_task, update_task


@receiver(post_save, sender=Newsletter)
def after_create_newsletter(sender, created, instance, **kwargs):
    if instance:
        if created:
            create_task(instance)
        else:
            update_task(instance)

