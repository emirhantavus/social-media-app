from django.shortcuts import render
from posts.models import Post
from posts.serializers import PostSerializer
from rest_framework import generics , status
from rest_framework import permissions
from django.core.exceptions import PermissionDenied
from rest_framework.response import Response

class PostListView(generics.ListCreateAPIView):
      permission_classes = [permissions.AllowAny,]
      queryset = Post.objects.all().order_by('-created_at')
      serializer_class = PostSerializer
      
      def perform_create(self, serializer):
            serializer.save(author=self.request.user)
            
class PostRetrieveUpdateAndDestroyView(generics.RetrieveDestroyAPIView):
      permission_classes = [permissions.IsAuthenticated]
      queryset = Post.objects.all()
      serializer_class = PostSerializer
      
      def perform_update(self,serializer):
            if self.request.user != serializer.instance.author:
                  raise PermissionDenied("U can only edit your own posts")
            serializer.save()
            return Response({'message':'Post edited successfuly'},status.HTTP_200_OK)
            
      def perform_destroy(self, instance):
            if self.request.user != instance.author:
                  raise PermissionDenied("U can only delete your own posts")
            instance.delete()
            
      def delete(self, request, *args,**kwargs):
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response({'message':'Post deleted successfuly'},status.HTTP_200_OK)
      