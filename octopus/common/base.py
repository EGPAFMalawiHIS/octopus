import uuid

from django.db import models


class UuidField(models.CharField):
    """A version 4 UUID field"""

    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = 128
        kwargs["default"] = uuid.uuid4

        if "unique" not in kwargs:
            kwargs["unique"] = True
        if "null" not in kwargs:
            kwargs["null"] = False

        super(type(self), self).__init__(*args, **kwargs)


class BaseModel(models.Model):
    """Common fields"""

    class Meta:
        abstract = True

    uuid = UuidField()
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True)
