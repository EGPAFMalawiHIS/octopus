from django.utils.translation import pgettext_lazy

__version__ = "0.1.0"
__version_info__ = tuple(
    int(num) if num.isdigit() else num
    for num in __version__.replace("-", ".", 1).split(".")
)


class QueueStatus:
    """Flags for queue status"""

    QUEUED = "Queued"
    SENT = "Sent"
    FAILED = "Failed"

    CHOICES = [
        (QUEUED, pgettext_lazy("queue status", "Queued")),
        (SENT, pgettext_lazy("queue status", "Sent")),
        (FAILED, pgettext_lazy("queue status", "Failed")),
    ]
