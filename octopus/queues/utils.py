import logging
from typing import Any

from . import exceptions, models


def get_source_from_ip(ip_address: str) -> Any:
    """
    Gets the source from ip_address

    [TODO] remove models.Source, find better implementation - coupling!
    """

    logging.info("Retrieving source from IP address, %s", ip_address)

    try:
        source_obj = models.Source.objects.get(address=ip_address)

    except models.Source.DoesNotExist:
        raise exceptions.SourceNotFound(
            f"No source found matching IP address, {ip_address}"
        )

    return source_obj
