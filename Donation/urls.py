from django.urls import path
# from rest_framework import views
from django.contrib import admin

# from .views import ProductViewSet
from . import *


from pickle import GET
from django.contrib import admin
from django.urls import path
from .views import *
from  rest_framework import permissions
# from  rest_framework.decorators import api_view,permission_classes


urlpatterns = [
    path('category', CategoryViewSet.as_view(), name='category'),
    # path('', homepage),
    #  path('product', ProductViewSet.as_view({'get': 'list'}), name='product'),
]

