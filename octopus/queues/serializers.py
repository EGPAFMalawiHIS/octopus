import logging

from rest_framework import serializers

from . import exceptions, models, utils


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

            validated_data["source"] = utils.get_source_from_ip(ip_address)

            logging.info(
                "The IP address, %s, is mapped to %s as it's source",
                ip_address,
                validated_data["source"],
            )

        except exceptions.SourceNotFound:
            logging.info("No registered source found for %s", ip_address)
            return

        return super().create(validated_data)
