from rest_framework import serializers
from comments.models import Comment

class CommentSerializer(serializers.ModelSerializer):
      author = serializers.StringRelatedField(read_only=True)
      class Meta:
            model = Comment
            fields = ['id','author','post','content','created_at']
            read_only_fields = ['post','author']