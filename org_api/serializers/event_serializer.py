from rest_framework import serializers
from org_api.models import Event

from org_api.serializers import OrganizerSerializer

class EventSerializer(serializers.ModelSerializer):
    org = OrganizerSerializer()

    class Meta:
        model = Event
        fields = ('id', 'title', 'date', 'readable_date','readable_time', 'time', 'private', 'org')
