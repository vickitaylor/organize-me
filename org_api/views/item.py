import uuid
import base64
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from django.core.files.base import ContentFile
from org_api import serializers

from org_api.models import Item, Organizer, Category
from org_api.serializers import ItemSerializer


class ItemView(ViewSet):
    """ Organize Me Item View """

    def list(self, request):
        """ Handles the GET request, to get all items from the database, sorted in ascending order by name.

        Returns:
            Response: JSON serialized list of items
        """

        items = Item.objects.all().order_by("name")
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk):
        """ Handles the GET request to get a single item, if the selected key is not found then a 404 message is returned

        Returns:
            Response: JSON serialized list of the item for the selected key
        """

        try:
            item = Item.objects.get(pk=pk)
            serializer = ItemSerializer(item)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Item.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        """ Handles the POST request to create a new item.

        Returns:
            Response: JSON serialized item instance
        """

        organizer = Organizer.objects.get(user=request.auth.user)
        category = Category.objects.get(pk=request.data["category"])

        format, imgstr = request.data["picture"].split(';base64')
        ext = format.split('/')[-1]
        data = ContentFile(base64.b64decode(
            imgstr), name=f'{request.data["name"]}--{uuid.uuid4()}.{ext}')

        item = Item.objects.create(
            name=request.data["name"],
            org=organizer,
            picture=data,
            private=False,
            description=request.data["description"],
            category=category
        )
        serializer = ItemSerializer(item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """ Handles the PUT request for the selected item. 

        Returns:
            Response: Empty body with a 204 status code
        """

        item = Item.objects.get(pk=pk)

        format, imgstr = request.data["picture"].split(';base64')
        ext = format.split('/')[-1]
        data = ContentFile(base64.b64decode(
            imgstr), name=f'{request.data["name"]}--{uuid.uuid4()}.{ext}')

        item.name = request.data["name"]
        item.picture = data
        item.private = False
        item.description = request.data["description"]
        item.category = Category.objects.get(pk=request.data["category"])

        item.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
