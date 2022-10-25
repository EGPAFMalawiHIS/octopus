import logging

from django.db.models.signals import post_save
from django.dispatch import receiver

from octopus.octopus.queues import exceptions
from octopus.routes import RouteType
from octopus.routes.models import Route

from . import models, routing


@receiver(post_save, sender=models.QueueItem)
def queue_item_created(sender, instance, created, **kwargs):
    """runs when an item is created in the queue"""

    USE_INTERNET_OR_VPN_ROUTE = True

    if created:

        logging.info("Item from %s has been added in the queue.", instance.source.name)

        # get all registered routes
        registered_routes = Route.objects.all().order_by("weight")

        # get routes based on weighting
        try:
            routes = routing.get_weighted_routes(registered_routes)

            for route in routes:
                if route[RouteType.INTERNET_OR_VPN]:

                    USE_INTERNET_OR_VPN_ROUTE = routing.is_available(
                        route[RouteType.INTERNET_OR_VPN]["destination"]
                    )

        except exceptions.NoRegisteredRoutesFound:

            logging.error("No registered routes found.")

        # send data
        logging.info("USE_INTERNET_OR_VPN_ROUTE: %s", USE_INTERNET_OR_VPN_ROUTE)
        logging.info("Preparing to send data to peer")
