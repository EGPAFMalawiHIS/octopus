import logging

from rest_framework import serializers

from . import models


class QueueItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.QueueItem
        fields = [
            "id",
            "item_id",
            "payload",
        ]

    def create(self, validated_data):

        ip_address = self.context.get("request").META.get("REMOTE_ADDR")

        logging.info("Looking for registered source for %s", ip_address)

        try:

            validated_data["source"] = models.Source.objects.get(address=ip_address)

            logging.info(
                "The IP address, %s, is mapped to %s as it's source",
                ip_address,
                validated_data["source"],
            )

        except (models.Source.DoesNotExist, AssertionError):
            logging.info("No registered source found for %s", ip_address)
            raise serializers.ValidationError(
                {
                    "status": "error",
                    "message": f"No registered source found for {ip_address}",
                }
            )

        return super().create(validated_data)
