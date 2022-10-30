from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class SellImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellImage
        fields = '__all__'

class SellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sell
        fields = '__all__'

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'

class PurchaseImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseImage
        fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class UserFavoriteAdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFavoriteAds
        fields = '__all__'