from rest_framework import serializers
from django.contrib.auth.models import User

from org_api.models import Organizer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username')

class OrganizerSerializer(serializers.ModelSerializer):
    
    user = UserSerializer()

    class Meta:
        model = Organizer
        fields = ('id', 'user', 'picture', 'approved')