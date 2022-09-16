from rest_framework import serializers
from org_api.models import Room

from org_api.serializers.user_serializer import OrganizerSerializer


class RoomSerializer(serializers.ModelSerializer):

    org = OrganizerSerializer()

    class Meta:
        model = Room
        fields = ('id', 'name', 'org', 'picture', 'private')
