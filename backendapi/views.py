from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProductSerializers
from .models import Product

# Create your views here.

class ProductView(viewsets.ModelViewSet):
    serializer_class = ProductSerializers
    queryset = Product.objects.all()