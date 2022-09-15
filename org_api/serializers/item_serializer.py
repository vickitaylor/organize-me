from rest_framework import serializers
from org_api.models import Item, ItemDetail, Like

from org_api.serializers import OrganizerSerializer
from org_api.serializers.status_serializer import StatusSerializer

class ItemSerializer(serializers.ModelSerializer):
    org = OrganizerSerializer()

    class Meta:
        model = Item
        fields = ('id', 'name', 'description', 'category', 'liked', 'private', 'picture', 'org')



class ItemDetailSerializer(serializers.ModelSerializer):
    item = ItemSerializer()
    status = StatusSerializer()

    class Meta:
        model = ItemDetail
        fields = ('id', 'quantity', 'receipt_pic', 'purchased_from', 'serial_num', 'purchase_date', 'expiration_date', 'price', 'item', 'room', 'status')
