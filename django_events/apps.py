from django.apps import AppConfig
from django.conf import settings


class DjangoEventsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_events'

    def ready(self, *args, **kwargs):
        super().ready(args, kwargs)

