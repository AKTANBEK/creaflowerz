from rest_framework import serializers
from .models import Flower, Category


class FlowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flower
        fields = ['id', 'name', 'image', 'old_price', 'price', 'description', 'size']


class CategorySerializer(serializers.ModelSerializer):
    flowers = FlowerSerializer(many=True)

    class Meta:
        model = Category
        fields = ['id', 'title', 'flowers']
