from django.shortcuts import render
from rest_framework import generics
from .models import Flower, Category
from .serializers import CategorySerializer


class FlowerAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
