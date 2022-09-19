import uuid
import base64
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from django.core.files.base import ContentFile
from django.db.models.functions import Lower

from org_api.models import ItemDetail, Item, Room, Status
from org_api.serializers import ItemDetailSerializer


class ItemDetailView(ViewSet):
    """ Organize Me Item Detail View """

    def list(self, request):
        """ Handles the GET request, to get all items with extra properties from the database, sorted in ascending order by name.
        - Query param being used to get the items in a room.

        Returns:
            Response: JSON serialized list of items
        """

        room = request.query_params.get('room', None)

        if room is not None:
            items = ItemDetail.objects.filter(
                room=room).order_by(Lower("item__name"))

        else:
            items = ItemDetail.objects.all().order_by(Lower("item__name"))

        serializer = ItemDetailSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        """ Handles the GET request to get a single items details, if the selected key is not found then a 404 message is returned

        Returns:
            Response: JSON serialized list of the item for the selected key
        """

        try:
            item = ItemDetail.objects.get(pk=pk)
            serializer = ItemDetailSerializer(item)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ItemDetail.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        """ Handles the POST request to create a new item detail.

        Returns:
            Response: JSON serialized item detail instance
        """
        item = Item.objects.get(pk=request.data["item"])
        room = Room.objects.get(pk=request.data["room"])

        item_detail = ItemDetail.objects.create(
            item=item,
            room=room,
            quantity=1
        )

        serializer = ItemDetailSerializer(item_detail)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """ Handles the PUT request for the selected item details. 

        Returns:
            Response: Empty body with a 204 status code
        """

        item_detail = ItemDetail.objects.get(pk=pk)

        try:
            format, imgstr = request.data["receipt_pic"].split(';base64')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(
                imgstr), name=f'{request.data["purchased_from"]}--{uuid.uuid4()}.{ext}')

            item_detail.room = Room.objects.get(pk=request.data["room"])
            item_detail.quantity = request.data["quantity"]
            item_detail.purchased_from = request.data["purchased_from"]
            item_detail.price = float(request.data["price"])
            item_detail.status = Status.objects.get(pk=request.data["status"])
            item_detail.serial_num = request.data["serial_num"]
            item_detail.purchase_date = request.data["purchase_date"]
            item_detail.expiration_date = request.data["expiration_date"]
            item_detail.receipt_pic = data

        except ValueError as ex:
            item_detail.room = Room.objects.get(pk=request.data["room"])
            item_detail.quantity = request.data["quantity"]
            item_detail.purchased_from = request.data["purchased_from"]
            item_detail.price = float(request.data["price"])
            item_detail.status = Status.objects.get(pk=request.data["status"])
            item_detail.serial_num = request.data["serial_num"]
            item_detail.purchase_date = request.data["purchase_date"]
            item_detail.expiration_date = request.data["expiration_date"]

        item_detail.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
