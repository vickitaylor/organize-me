from rest_framework import serializers
from org_api.models import Item

from org_api.serializers import OrganizerSerializer

class ItemSerializer(serializers.ModelSerializer):
    org = OrganizerSerializer()

    class Meta:
        model = Item
        fields = ('id', 'name', 'description', 'category','likes', 'private', 'picture', 'org')
