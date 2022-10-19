from django.contrib import admin

from . import models


@admin.register(models.Source)
class SourceAdmin(admin.ModelAdmin):
    pass


@admin.register(models.QueueItem)
class QueueAdmin(admin.ModelAdmin):
    pass
