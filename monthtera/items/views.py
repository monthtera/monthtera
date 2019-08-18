from rest_framework import viewsets

from .models import Item
from .serializers import ItemSerializer


class ItemViewset(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


def items(request):
    return Item.objects.all()
