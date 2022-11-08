import logging
import os

from django.db.models.signals import post_save
from django.dispatch import receiver

from octopus.queues import exceptions
from octopus.routes import RouteType
from octopus.routes.models import Route

from . import formats, models, routing


@receiver(post_save, sender=models.QueueItem)
def queue_item_created(sender, instance, created, **kwargs):
    """runs when an item is created in the queue"""

    if created:

        logging.info("Item from %s has been added in the queue.", instance.source.name)

        # get all registered routes
        registered_routes = Route.objects.all().order_by("weight")

        # get routes based on weighting

        try:
            # this will bring 2 routes, the primary and fallback
            route = {}
            payload = {}
            routes = routing.get_weighted_routes(registered_routes)

            if routes[RouteType.INTERNET_OR_VPN]["destination"]:
                route = routes[RouteType.INTERNET_OR_VPN]
                payload = instance.payload

            else:
                route = routes[RouteType.SMS]
                formats.SMS_DATA_FORMAT["tasks"][0]["to"] = os.environ.get("SHORTCODE")
                formats.SMS_DATA_FORMAT["tasks"][0]["sms"] = instance.payload
                payload = formats.SMS_DATA_FORMAT

            logging.info("Using destination %s", route["destination"])

            send_data = routing.send_data(
                endpoint=route["destination"],
                payload=payload,
                headers={"Content-type": "application/json; charset=utf-8"},
            )

            logging.info(send_data)

        except exceptions.NoRegisteredRoutesFound:

            logging.error("No registered routes found.")
