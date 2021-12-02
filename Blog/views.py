from django.shortcuts import render
from .serializers import PostSerializer, CommentSerializer, CategorySerializer
from .models import Post, Comment, Category
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.generics import GenericAPIView, mixins, ListCreateAPIView, RetrieveUpdateDestroyAPIView





# Create your views here.
class PostMVS(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


 
class CommentMVS(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CategoryMVS(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
