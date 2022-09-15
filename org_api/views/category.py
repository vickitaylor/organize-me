from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from django.db.models.functions import Lower

from org_api.models import Category
from org_api.serializers import CategorySerializer


class CategoryView(ViewSet):
    """ Organize Me Category View """

    def list(self, request):
        """ Handles the GET request, to get all categories from the database, sorted in ascending order by name.

        Returns:
            Response: JSON serialized list of categories
        """

        categories = Category.objects.all().order_by(Lower("name"))
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
