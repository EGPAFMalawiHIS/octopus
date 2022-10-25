from django.utils.translation import pgettext_lazy


class RouteStatus:
    """Flags for route reachability"""

    UP = "Up"
    DOWN = "Down"
    UNKNOWN = "Unknown"

    CHOICES = [
        (UP, pgettext_lazy("route status", "Up")),
        (DOWN, pgettext_lazy("route status", "Down")),
        (UNKNOWN, pgettext_lazy("route status", "Unknown")),
    ]


class RouteType:
    """Type of route"""

    INTERNET_OR_VPN = "Internet"
    SMS = "SMS"

    CHOICES = [
        (INTERNET_OR_VPN, pgettext_lazy("route type", "Internet or VPN")),
        (SMS, pgettext_lazy("route type", "SMS")),
    ]
