from rest_framework import serializers
from posts.models import Post

class PostSerializer(serializers.ModelSerializer):
      class Meta:
            model = Post
            fields = ['id', 'author', 'content_type', 'content', 'media', 'created_at', 'updated_at']
            read_only_fields = ['id', 'author', 'created_at', 'updated_at']