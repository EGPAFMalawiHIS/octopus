import logging
import platform
import subprocess
from typing import Any

import requests

from octopus.routes import RouteType

from . import exceptions

# Routes


def get_weighted_routes(routes) -> dict[str, str]:
    """Gets the default and fallback routes.

    Args:
        routes (dict[str,str]): Queryset of registered routes

    Returns:
        dict[str,str]: Primary and fallback routes
    """

    primary_fallback_routes = {
        RouteType.INTERNET_OR_VPN: {
            "uuid": "",
            "address": "",
            "destination": "",
            "weight": 0,
        },
        RouteType.SMS: {
            "uuid": "",
            "address": "",
            "destination": "",
            "weight": 0,
        },
    }

    if not routes:
        logging.info("No registered routes found.")
        raise exceptions.NoRegisteredRoutesFound("No registered routes found")

    for route in routes:

        # if the route has a higher weighting
        # and the route is available [successfully pinged]
        # then that route is available
        if route.weight > primary_fallback_routes[route.type][
            "weight"
        ] and is_available(route.address):

            primary_fallback_routes[route.type]["uuid"] = route.uuid
            primary_fallback_routes[route.type]["address"] = route.address
            primary_fallback_routes[route.type]["destination"] = route.destination
            primary_fallback_routes[route.type]["weight"] = route.weight

    return primary_fallback_routes


def is_available(address: str) -> bool:
    """Checks if destination can be reached via the route

    Args:
        address (str): Address of the destination

    Returns:
        bool: True if destination can be reached through the route, otherwise False
    """

    param = "-n" if platform.system().lower() == "windows" else "-c"

    if subprocess.call(["ping", param, "1", address]) != 0:

        return False

    return True


# Sending data


def send_data(endpoint: str, payload: Any, headers: dict[str, str] = None) -> bool:
    """Sends data using an HTTP route

    Args:
        routes (list): available routes
        payload (Any): data to be sent

    Returns:
        bool: True if data is sent successfully
    """

    try:
        r = requests.post(endpoint, json=payload, headers=headers)

    except Exception as e:
        logging.error("Failed to send data to %s with exception %s", e, endpoint)
        return False

    else:
        r.raise_for_status()
        logging.info("Data sent successfully to %s,", endpoint)
        logging.info("Response %s: ", r.json())
        return True
