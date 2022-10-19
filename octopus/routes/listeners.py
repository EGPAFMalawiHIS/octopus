import logging

from django.db.models.signals import post_save
from django.dispatch import receiver

from . import models


@receiver(post_save, sender=models.Route)
def route_created(sender, instance, created, **kwargs):
    """runs when a route is created"""

    logging.info("%s route has been successfully created", instance.name)
