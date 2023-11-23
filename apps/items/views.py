import typing
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from .models import Item
from .serializers import ItemSerializer


class ItemAPI(GenericViewSet, CreateModelMixin, RetrieveModelMixin):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
      
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)