from nis import cat
from unicodedata import category
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

    def create(self, request):
        """ Handles the POST request to create a new category.

        Returns:
            Response: JSON serialized category instance
        """

        category = Category.objects.create(
            name=request.data["name"]
        )
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
