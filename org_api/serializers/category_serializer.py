from rest_framework import serializers
from org_api.models import Category

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ('id', 'name')
