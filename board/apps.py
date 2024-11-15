from django.apps import AppConfig
from django.db.models.signals import post_save


class BoardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'board'

    def ready(self):
        from . import signals