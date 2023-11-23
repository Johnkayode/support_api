from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.items.views import ItemAPI


router = DefaultRouter(trailing_slash=False)
router.register("items", ItemAPI, "item")

urlpatterns = [
] + router.urls

