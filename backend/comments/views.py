from django.shortcuts import render
from comments.models import Comment
from posts.models import Post
from comments.serializers import CommentSerializer
from rest_framework import generics , status , permissions
from django.core.exceptions import PermissionDenied
from rest_framework.response import Response


class CommentCreateView(generics.CreateAPIView):
      serializer_class = CommentSerializer
      permission_classes = [permissions.IsAuthenticatedOrReadOnly]
      
      def get_queryset(self):
            post_id = self.kwargs.get('post_id')
            return Comment.objects.filter(post=post_id)
      
      def perform_create(self, serializer):
            post_id = self.kwargs.get('post_id')
            post = Post.objects.get(id=post_id)
            serializer.save(author=self.request.user,post=post)
            

class CommentRetrieveUpdateAndDestroyView(generics.RetrieveDestroyAPIView):
      permission_classes = [permissions.IsAuthenticated]
      queryset = Comment.objects.all()
      serializer_class = CommentSerializer
      
      def perform_update(self,serializer):
            if self.request.user != serializer.instance.author:
                  raise PermissionDenied("U can only edit your own comments")
            serializer.save()
            return Response({'message':'Comment edited successfuly'},status.HTTP_200_OK)
            
      def perform_destroy(self, instance):
            if self.request.user != instance.author:
                  raise PermissionDenied("U can only delete your own comments")
            instance.delete()
            
      def delete(self,request,*args,**kwargs):
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response({'message':'Comment deleted successfuly'},status.HTTP_200_OK)