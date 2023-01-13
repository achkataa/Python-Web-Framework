from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers, permissions

from django_rest.api.models import Product, Category


# class ProductsListView(APIView):
#     def get(self, request):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(data=serializer.data)
#
#     def post(self, request):
#         serializer = ProductSerializer(data=request.data, many=False)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data)
#         return Response(serializer.errors, status=404)



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("category_name", )

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(many=False)
    class Meta:
        model = Product
        fields = '__all__'

class ProductsListView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    permission_classes = (
        permissions.IsAuthenticated,
    )
class CategoriesListVIew(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
