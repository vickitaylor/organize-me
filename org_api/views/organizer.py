from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.contrib.auth.models import User


from org_api.models import Organizer
from org_api.serializers import OrganizerSerializer

class OrganizerView(ViewSet):
    """Organizer Me Organizer User view"""

    def retrieve(self, request, pk):
        """handle GET request for a single user
        """

        try:
            user = Organizer.objects.get(pk=pk)
            serializer = OrganizerSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Organizer.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

