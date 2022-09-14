from rest_framework import serializers
from org_api.models import Item, ItemDetail

from org_api.serializers import OrganizerSerializer

class ItemSerializer(serializers.ModelSerializer):
    org = OrganizerSerializer()

    class Meta:
        model = Item
        fields = ('id', 'name', 'description', 'category','likes', 'private', 'picture', 'org')


class ItemDetailSerializer(serializers.ModelSerializer):
    item = ItemSerializer()

    class Meta:
        model = ItemDetail
        fields = ('id', 'quantity', 'receipt_pic', 'purchased_from', 'serial_num', 'purchase_date', 'expiration_date', 'item', 'room', 'status')
