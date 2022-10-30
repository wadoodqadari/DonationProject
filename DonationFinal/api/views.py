from django.shortcuts import render, HttpResponse
from .serializers import *
from rest_framework import generics

from .models import *

# Create your views here.



class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetial(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetial(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetial(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class SellImageList(generics.ListCreateAPIView):
    queryset = SellImage.objects.all()
    serializer_class = SellImageSerializer

class SellImageDetial(generics.RetrieveUpdateDestroyAPIView):
    queryset = SellImage.objects.all()
    serializer_class = SellImageSerializer

class SellList(generics.ListCreateAPIView):
    queryset = Sell.objects.all()
    serializer_class = SellSerializer

class SellDetial(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sell.objects.all()
    serializer_class = SellSerializer

class PurchaseImageList(generics.ListCreateAPIView):
    queryset = PurchaseImage.objects.all()
    serializer_class = PurchaseImageSerializer

class PurchaseImageDetial(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseImage.objects.all()
    serializer_class = PurchaseImageSerializer



class PurchaseList(generics.ListCreateAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

class PurchaseDetial(generics.RetrieveUpdateDestroyAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

class AddressList(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
class AddressDetial(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer    


class UserFavoriteAdsList(generics.ListCreateAPIView):
    queryset = UserFavoriteAds.objects.all()
    serializer_class = UserFavoriteAdsSerializer
class UserFavoriteAdsDetial(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserFavoriteAds.objects.all()
    serializer_class = UserFavoriteAdsSerializer