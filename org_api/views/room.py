import uuid
import base64
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from django.core.files.base import ContentFile

from org_api.models import Room
from org_api.models import Organizer
from org_api.serializers import RoomSerializer


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

        else:
            rooms = Room.objects.all().order_by("name")

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

    def create(self, request):
        """ Handles the POST request to create a new room for the user.

        Returns:
            Response: JSON serialized room instance
        """

        organizer = Organizer.objects.get(user=request.auth.user)

        format, imgstr = request.data["picture"].split(';base64')
        ext = format.split('/')[-1]
        data = ContentFile(base64.b64decode(
            imgstr), name=f'{request.data["name"]}--{uuid.uuid4()}.{ext}')

        room = Room.objects.create(
            name=request.data["name"],
            org=organizer,
            picture=data,
            private=False
        )
        serializer = RoomSerializer(room)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """ Handles the PUT request for the selected room. 

        Returns:
            Response: Empty body with a 204 status code
        """

        room = Room.objects.get(pk=pk)

        format, imgstr = request.data["picture"].split(';base64')
        ext = format.split('/')[-1]
        data = ContentFile(base64.b64decode(
            imgstr), name=f'{request.data["name"]}--{uuid.uuid4()}.{ext}')

        room.name = request.data["name"]
        room.picture = data

        room.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
