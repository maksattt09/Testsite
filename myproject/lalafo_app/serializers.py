from .models import Category, Product
from rest_framework import serializers


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name', 'category_image']


class ProductSerializers(serializers.ModelSerializer):
     class Meta:
         model = Product
         fields = ['id', 'product_name', 'price', 'owner', 'product_image', 'product_type', 'phone_number', 'description', 'created_date']