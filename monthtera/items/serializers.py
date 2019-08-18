from rest_framework import serializers
from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('name', 'brand', 'cycle', 'price', 'channel', 'how_to_cancel')
