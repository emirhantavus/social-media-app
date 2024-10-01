from django.db import models
from django.contrib.auth import get_user_model
from posts.models import Post

user = get_user_model()

class Comment(models.Model):
      post = models.ForeignKey(
            Post,
            related_name='comments',
            on_delete=models.CASCADE
      )
      
      author = models.ForeignKey(
            user,
            related_name='commnets',
            on_delete=models.CASCADE
      )
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      
      def __str__(self):
            return f"comment by {self.author.email} on {self.post.id}"