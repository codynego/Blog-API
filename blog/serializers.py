from rest_framework import serializers
from .models import Post, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'created', 'updated', 'category')
        
    def create(self, validated_data):
        category_data = validated_data.pop('category')
        category_serializer = CategorySerializer(data=category_data)
        category_serializer.is_valid(raise_exception=True)
        category = category_serializer.save()
        post = Post.objects.create(category=category, **validated_data)
        return post
    
		
