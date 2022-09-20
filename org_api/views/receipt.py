import uuid
import base64
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from django.core.files.base import ContentFile

from org_api.models import Receipt, ItemDetail
from org_api.serializers import ReceiptSerializer


class ReceiptView(ViewSet):
    """ Organize Me Item Receipt picture View """

    def list(self, request):
        """ Handles the GET request, for the receipt pictures.

        Returns:
            Response: JSON serialized list of items
        """

        pictures = Receipt.objects.all()

        serializer = ReceiptSerializer(pictures, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        """ Handles the GET request for a receipt picture.

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
        """ Handles the POST request to create a receipt picture detail.

        Returns:
            Response: JSON serialized receipt instance
        """

        item = ItemDetail.objects.get(pk=request.data["item"])

        format, imgstr = request.data["picture"].split(';base64')
        ext = format.split('/')[-1]
        data = ContentFile(base64.b64decode(
            imgstr), name=f'{request.data["name"]}--{uuid.uuid4()}.{ext}')

        receipt = Receipt.objects.create(
            receipt_pic=data,
            item_detail=item
        )

        serializer = ReceiptSerializer(receipt)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """ Handles the PUT request for the selected receipt picture. 

        Returns:
            Response: Empty body with a 204 status code
        """

        receipt = Receipt.objects.get(pk=pk)

        format, imgstr = request.data["receipt_pic"].split(';base64')
        ext = format.split('/')[-1]
        data = ContentFile(base64.b64decode(
            imgstr), name=f'{request.data["name"]}--{uuid.uuid4()}.{ext}')

        receipt.receipt_pic = data

        receipt.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
