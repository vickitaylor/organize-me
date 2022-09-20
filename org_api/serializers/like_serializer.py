from rest_framework import serializers
from org_api.models import Like

from org_api.serializers.item_serializer import ItemSerializer
from org_api.serializers.user_serializer import OrganizerSerializer


class LikeSerializer(serializers.ModelSerializer):
    org = OrganizerSerializer()
    item = ItemSerializer()

    class Meta:
        model = Like
        fields = ('id', 'item', 'org')
