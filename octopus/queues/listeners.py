import logging

from django.db.models.signals import post_save
from django.dispatch import receiver

from . import models


@receiver(post_save, sender=models.QueueItem)
def queue_item_created(sender, instance, created, **kwargs):
    """runs when an item is created in the queue"""

    if created:
        logging.info("Item from %s has been added in the queue", instance.source.name)
