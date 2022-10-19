from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from octopus.queues.views import QueueViewSet
from octopus.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("queue", QueueViewSet)


app_name = "api"
urlpatterns = router.urls
