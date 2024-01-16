import os
import sys
from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    def ready(self) -> None:
        from . import receivers
        from django.contrib.auth.models import User
        from django.db.utils import IntegrityError
        from .services.celery.services import create_task_for_mailing

        if 'migrate' not in sys.argv:

            # Создание суперпользователя
            try:
                User.objects.create_superuser(
                    os.environ.get("ADMIN_USERNAME", "admin"),
                    os.environ.get("ADMIN_EMAIL", 'admin@example.com'),
                    os.environ.get("ADMIN_PASSWORD", "admin"))
                print('Superuser created successfully!')
            except IntegrityError:
                print('Superuser already exists.')

            # создание расписания для отправки отчета на почту
            try:
                create_task_for_mailing()
            except IntegrityError:
                print("task already exists")

