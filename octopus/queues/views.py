import logging

from django.db import transaction
from rest_framework import viewsets

from . import models, serializers

logger = logging.getLogger(__name__)


class QueueViewSet(viewsets.ModelViewSet):
    """Item queuing"""

    queryset = models.QueueItem.objects.all().order_by("-created_at")

    serializer_class = serializers.QueueItemSerializer

    def perform_create(self, serializer: serializers.QueueItemSerializer):

        with transaction.atomic():

            queue_item: models.QueueItem = serializer.save()

            logger.info("Queued item from %s", queue_item.source.get_source_name)
