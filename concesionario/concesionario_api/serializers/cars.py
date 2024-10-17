from rest_framework import serializers

from autos.models import Category, Car, CarReview
from usuarios.models import User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'name',
            'pk',
        )


class CarSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    description = serializers.SerializerMethodField()

    class Meta:
        model = Car
        fields = (
            'name',
            'pk',
            'brand',
            'stock',
            'category',
            'description',
            'price',
            'stock',
        )

    def get_description(self, value):
        if value.description is None:
            return "No posee descripción"
        return value.description

    def update(self, instance, validated_data):
        category_data = validated_data.pop(
            'category', None
        )
        category, _= Category.objects.get_or_create(
          **category_data
        )

        instance.category = category

        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.active = validated_data.get('active', instance.active)

        instance.save()
        return instance
    

class CarReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarReview
        fields = (
            'car',
            'author',
            'text',
            'date',
            'rating',
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']

