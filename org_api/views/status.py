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
