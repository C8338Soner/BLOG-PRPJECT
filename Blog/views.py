from django.shortcuts import render
from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.generics import GenericAPIView, mixins, ListCreateAPIView, RetrieveUpdateDestroyAPIView





# Create your views here.
class PostMVS(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    
    # def get_queryset(self):
    #     queryset = Post.objects.all()
    #     category = self.kwargs["category"]  # backend, frontend
    #     queryset = queryset.filter(category__name=category)
    #     return queryset



 
class CommentMVS(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
