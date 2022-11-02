# from itertools import product

from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView


from .models import Category, Product
from .serializers import ProductSerializer,CategorySerializer
from rest_framework import viewsets

# Create your views here.


def homepage(request):
	# data = Jobs.objects.all()
	# context= {
	# 	'data':data
	# }
	# print(data)
    return render(request, 'frontend/index.html')

	# return render(request,"home.html")

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer




class CategoryViewSet(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

# class ProductUpdate(generics.RetrieveUpdateDestroyAPIView):
#     queryset=Product
#     serializer_class=ProductSerializer






















# from rest_framework.decorators import api_view
# from rest_framework.response import Response


# @api_view(['GET'])
# # create your views here 
# def apioverview(request):
#     api_urls={
#     'this is get data in api',
#     'this is get and post method in api'
#     }
#     return Response(api_urls)

# @api_view(['GET'])
# def Proview(request):
#     product=Product.objects.all()
#     serlizer=ProductSerializer(product,many=True)
#     return Response(serlizer.data)


# @api_view(['GET'])
# def Prosearch(request,pk):
#     product=Product.objects.get(id=pk)
#     serlizer=ProductSerializer(product,many=False)
#     return Response(serlizer.data)   



# @api_view(['POST'])
# def Procreate(request):
#     # product=Product.objects.get(id=pk)
#     serlizer=ProductSerializer(data=request.data)

#     if serlizer.is_valid():
#         serlizer.save()

#     return Response(serlizer.data)   



# @api_view(['POST'])
# def Proupdate(request,pk):
#     produc=Product.objects.get(id=pk)
#     serlizer=ProductSerializer(instance=produc,data=request.data)

#     if serlizer.is_valid():
#         serlizer.save()

#     return Response(serlizer.data)   








