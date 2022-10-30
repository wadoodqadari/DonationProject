from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('category/', CategoryList.as_view(), name='Product'),
    path('category/<pk>/', CategoryDetial.as_view(), name='category_detial'),
    path('product/', ProductList.as_view(), name='product'),
    path('product/<pk>/', ProductDetial.as_view(), name='product_detial'),
    path('sell/image/', SellImageList.as_view(), name='sellimage'),
    path('sell/image/<pk>/', SellImageDetial.as_view(), name='sellimage_detial'),
    path('sell/', SellList.as_view(), name='sell'),
    path('sell/<int:pk>/', SellDetial.as_view(), name='sell_detial'),
    path('purchase/image/', PurchaseImageList.as_view(), name='purchaseimage'),
    path('purchase/image/<pk>/', PurchaseImageDetial.as_view(), name='purchaseimage_detial'),
    path('purchase/', PurchaseList.as_view(), name='purchase'),
    path('purchase/<int:pk>/', PurchaseDetial.as_view(), name='purchase_detial'),
    path('address/', AddressList.as_view(), name='address'),
    path('address/<int:pk>/', AddressDetial.as_view(), name='address_detial'),
    path('favorite/', UserFavoriteAdsList.as_view(), name='UserFavoriteAds'),
    path('favorite/<int:pk>/', UserFavoriteAdsDetial.as_view(), name='UserFavoriteAds_detial'),
]