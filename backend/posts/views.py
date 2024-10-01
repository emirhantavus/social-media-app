from django.shortcuts import render
from posts.models import Post
from posts.serializers import PostSerializer
from rest_framework import generics
from rest_framework import permissions

class PostList(generics.ListCreateAPIView):
      permission_classes = [permissions.IsAuthenticatedOrReadOnly]
      queryset = Post.objects.all().order_by('-created_at')
      serializer_class = PostSerializer
      
      def perform_create(self, serializer):
            serializer.save(author=self.request.user)