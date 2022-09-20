from rest_framework import serializers
from org_api.models import Receipt



class ReceiptSerializer(serializers.ModelSerializer):
    """JSON serializer for rating
    """
    class Meta:
        model = Receipt
        fields = ('id', 'item_detail', 'receipt_pic')
