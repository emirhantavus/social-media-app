from rest_framework import serializers
from categories.models import Category, Genre


class CategorySerializer(serializers.ModelSerializer):
      class Meta:
            model = Category
            fields = ['id','name']

class GenreSerializer(serializers.ModelSerializer):
      class Meta:
            model = Genre
            fields = ['id','name']
