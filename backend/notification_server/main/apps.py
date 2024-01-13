from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    def ready(self) -> None:
        from . import receivers

        from django.contrib.auth.models import User
        from django.db.utils import IntegrityError

        # Создание суперпользователя
        try:
            User.objects.create_superuser('admin', 'admin@example.com', 'admin')
            print('Superuser created successfully!')
        except IntegrityError:
            print('Superuser already exists.')

