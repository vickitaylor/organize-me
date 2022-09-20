from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from django.db.models.functions import Lower

from org_api.models import Like
from org_api.serializers import LikeSerializer


class LikeView(ViewSet):
    """ Organize Me Like View """

    def list(self, request):
        """ Handles the GET request, to get all liked items from the database, sorted in ascending order by name.

        Returns:
            Response: JSON serialized list of categories
        """

        user = request.query_params.get('user', None)

        if user is not None:
            items = Like.objects.filter(org=user).order_by(Lower("item__name"))
        serializer = LikeSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
