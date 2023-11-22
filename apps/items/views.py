import typing
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from .models import Item
from .serializers import ItemSerializer


class ItemAPI(GenericAPIView):
    serializer_class = ItemSerializer

    def get(self, request: Request, item_id: typing.Optional[int] = None) -> Response:
        # disallow GET requests without item_id
        if not item_id:
            return Response(
                {
                    "status_code": status.HTTP_405_METHOD_NOT_ALLOWED,
                    "error": "Method 'GET' not allowed.",
                },
                status=status.HTTP_405_METHOD_NOT_ALLOWED,
            )

        # retrieve item object
        try:
            item = Item.objects.get(id=item_id)
        except Item.DoesNotExist:
            return Response(
                {
                    "status_code": status.HTTP_404_NOT_FOUND,
                    "error": "Item does not exist",
                },
                status.HTTP_404_NOT_FOUND,
            )
        
        serializer = self.get_serializer(item)
        return Response(
            {
                "status_code": status.HTTP_201_CREATED,
                "data": serializer.data,
            },
            status.HTTP_200_OK,
        )

    def post(self, request: Request) -> Response:
        serializer = self.get_serializer(data=request.data)

        # validate serializer data
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "status_code": status.HTTP_201_CREATED,
                "data": serializer.data,
            },
            status.HTTP_201_CREATED,
        )
      