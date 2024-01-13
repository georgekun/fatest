
from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import Newsletter
from .services.views.services import create_connect_task, update_connect_task


@receiver(post_save, sender=Newsletter)
def after_save_newsletter(sender, created, instance, **kwargs):
    if instance:
        if created:
            create_connect_task(instance)
        else:
            update_connect_task(instance)


