from dataclasses import field, fields
from pyexpat import model
from rest_framework import serializers
from.models import Category, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields="__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields="__all__"