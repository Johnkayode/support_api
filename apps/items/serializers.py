from rest_framework.serializers import ModelSerializer

from apps.items.models import Item


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"
        required_fields = (
            "name",
            "price",
        )
        read_only_fields = (
            "created_at",
            "deleted_at",
        )
       