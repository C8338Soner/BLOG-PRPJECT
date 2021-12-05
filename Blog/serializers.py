from rest_framework import serializers
from .models import Post, Comment, Category

class PostSerializer(serializers.ModelSerializer):
  category = serializers.StringRelatedField()
  category_id = serializers.IntegerField()
  author = serializers.StringRelatedField()
  author_id = serializers.IntegerField()
  class Meta:
    model = Post
    fields = ('id', 'author', 'author_id', 'category', 'category_id', 'title', 'content', 'image', 'publish_date',
             'status', 'slug', 'comment_count', 'like_count')
 
class CommentSerializer(serializers.ModelSerializer):
 class Meta:
  model = Comment
  fields = '__all__'
  
  
class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'
