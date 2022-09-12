from datetime import date
from time import time
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

from org_api.models import Event
from org_api.models import Organizer
from org_api.serializers import EventSerializer


class EventView(ViewSet):
    """ Organize Me Event View """

    def list(self, request):
        """Handles the GET request to get all events in the database, sorted in order by date.
        - There is a query param to get the rooms only for the logged in user

        Returns:
            Response: JSON serialized list of rooms
        """

        user = request.query_params.get('user', None)

        if user is not None:
            events = Event.objects.filter(org=user).order_by('date')

        else:
            events = Event.objects.all().order_by("date")

        serializer = EventSerializer(events, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        """ Handles the GET request to a single event, if the selected key is not found 404 is returned

        Returns:
            Response:JSON serialized list of the room for the selected key
        """

        try:
            event = Event.objects.get(pk=pk)
            serializer = EventSerializer(event)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Event.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        """ Is the POST to create a new event for the user


        Returns:
            Response: JSON serialized event instance
        """

        organizer = Organizer.objects.get(user=request.auth.user)

        event = Event.objects.create(
            title=request.data["title"],
            date=request.data["date"],
            time=request.data["time"],
            private=False,
            org=organizer
        )

        serializer = EventSerializer(event)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """ Handles the PUT request for the selected event. 

        Returns:
        Response: Empty body with a 204 status code
        """

        event = Event.objects.get(pk=pk)

        event.title = request.data["title"]
        event.date = request.data["date"]
        event.time = request.data["time"]

        event.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """Handles the delete request for an event
        """

        event = Event.objects.get(pk=pk)
        event.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
