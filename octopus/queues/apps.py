import logging

from django.apps import AppConfig


class QueuesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "octopus.queues"

    def ready(self):
        import octopus.queues.listeners as listener

        logging.info(listener)
