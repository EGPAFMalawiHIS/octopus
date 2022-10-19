import logging

from django.apps import AppConfig


class RoutesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "octopus.routes"

    def ready(self) -> None:
        import octopus.routes.listeners as listener

        logging.info(listener)
