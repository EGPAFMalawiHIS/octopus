import os
from typing import Any

from django.core.exceptions import ObjectDoesNotExist
from django.db import models

from octopus.routes.models import BaseModel

from . import QueueStatus


class Source(BaseModel):
    """Where the data we are routing is coming from"""

    name = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True, blank=True)
    address = models.GenericIPAddressField(
        max_length=255, null=True, help_text="IP address of the source"
    )
    default_destination = models.CharField(max_length=255, null=True)
    default_retry_allowed = models.IntegerField(default=0)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        try:
            return str(self.name)
        except ObjectDoesNotExist:
            return "Unknown source"

    __repr__ = __str__

    @property
    def get_source_name(self) -> str:
        "Returns the name of the source."

        return str(self.name)

    @property
    def get_default_destination(self) -> str:
        """Returns the default destination"""

        return str(self.default_destination)


class QueueItem(BaseModel):
    """Queued items"""

    item_id = models.CharField(
        max_length=255,
        unique=True,
        help_text="ID created by source app to uniquely identify this item",
    )
    source = models.ForeignKey(Source, on_delete=models.SET_NULL, null=True)
    destination = models.CharField(max_length=255, null=True, blank=True)
    payload = models.TextField(null=True)
    encrypt_before_sending = models.BooleanField(default=True, verbose_name="encrypt")
    status = models.CharField(
        choices=QueueStatus.CHOICES,
        max_length=255,
        null=True,
        blank=True,
        default=QueueStatus.QUEUED,
    )
    retry_attempt_count = models.IntegerField(default=0)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        try:
            return f"Queue item from {self.source.name}"
        except ObjectDoesNotExist:
            return "Unknown queue item"

    __repr__ = __str__

    @property
    def allowed_retries(self) -> int:
        """Get how many times we should try to send the data from the queue to the destination"""

        if self.source.default_retry_allowed > os.environ.get(
            "DEFAULT_PUSH_RETRIES", 1
        ):
            return self.source.default_retry_allowed

        return os.environ.get("DEFAULT_PUSH_RETRIES", 1)

    def get_payload(self) -> Any:
        return self.payload

    def get_destination(self) -> Any:

        if self.destination:
            return self.destination

        return self.source.get_default_destination

    def encrypt(self) -> str:
        from cryptography.fernet import Fernet

        key = os.environ.get("ENCRYPTION_KEY", "SOME-VERY-COMPLICATED-ENCYPTION-KEY")
        fernet = Fernet(key)
        return fernet.encrypt(self.payload.encode())
