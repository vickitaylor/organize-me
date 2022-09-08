from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

from org_api.models import Room
from org_api.models.organizer import Organizer
from org_api.serializers import OrganizerSerializer, RoomSerializer


class RoomView(ViewSet):
    """ Organize Me Room View """

    def list(self, request):
        """ Handles the GET request, to get all rooms from the database, sorted in ascending order by name.
        - There is a query param to get the rooms only for the current user. 

        Returns:
            Response: JSON serialized list of rooms
        """
        
        user = request.query_params.get('user', None)
        
        if user is not None:
            rooms = Room.objects.filter(org=user).order_by("name")
            serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        """ Handles the GET request to get a single room, if the selected key is not found then a 404 message is returned
        
        Returns:
            Response: JSON serialized list of the room for the selected key
        """

        try:
            room = Room.objects.get(pk=pk)
            serializer = RoomSerializer(room)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Room.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
