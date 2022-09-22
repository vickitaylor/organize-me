from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from django.db.models.functions import Lower

from org_api.models import Status
from org_api.serializers import StatusSerializer


class StatusView(ViewSet):
    """ Organize Me Status View """

    def list(self, request):
        """ Handles the GET request, to get all item statuses from the database, sorted in ascending order by name.

        Returns:
            Response: JSON serialized list of item statuses
        """

        statuses = Status.objects.all().order_by(Lower("title"))
        serializer = StatusSerializer(statuses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        """ Handles the POST request to create a new item status.

        Returns:
            Response: JSON serialized status instance
        """

        new = Status.objects.create(
            title=request.data["title"]
        )
        serializer = StatusSerializer(new)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk):
        """Handles the delete request for an status
        """

        status = Status.objects.get(pk=pk)
        status.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)