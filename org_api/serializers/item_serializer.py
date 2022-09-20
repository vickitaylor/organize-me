from rest_framework import serializers
from org_api.models import Item, ItemDetail
from org_api.serializers.receipt import ReceiptSerializer

from org_api.serializers.user_serializer import OrganizerSerializer
from org_api.serializers.category_serializer import CategorySerializer
from org_api.serializers.status_serializer import StatusSerializer


class ItemSerializer(serializers.ModelSerializer):
    org = OrganizerSerializer()
    category = CategorySerializer()

    class Meta:
        model = Item
        fields = ('id', 'name', 'description', 'category',
                  'liked', 'private', 'picture', 'org')


class ItemDetailSerializer(serializers.ModelSerializer):
    item = ItemSerializer()
    status = StatusSerializer()
    receipt = ReceiptSerializer()

    class Meta:
        model = ItemDetail
        fields = ('id', 'quantity', 'receipt', 'purchased_from', 'serial_num',
                  'purchase_date', 'purchased_date', 'expiration_date', 'exp_date', 'price', 'item', 'room', 'status', 'format_price')
