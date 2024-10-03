from django.shortcuts import render
from comments.models import Comment
from comments.serializers import CommentSerializer
from rest_framework import generics , status , permissions
from django.core.exceptions import PermissionDenied
from rest_framework.response import Response


class CommentCreateView(generics.CreateAPIView):
      queryset = Comment.objects.all()
      serializer_class = CommentSerializer
      permission_classes = [permissions.IsAuthenticatedOrReadOnly]
      
      def perform_create(self, serializer):
            serializer.save(author=self.request.user)
            

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