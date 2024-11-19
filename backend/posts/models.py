from django.db import models
from django.contrib.auth import get_user_model


user = get_user_model()

class Post(models.Model):
      CONTENT_TYPES = (
            ('text','Text'),
            ('video','Video'),
            ('short','Short'),
      )
      
      author = models.ForeignKey(
            user,
            related_name='posts',
            on_delete=models.CASCADE
      )
      content_type = models.CharField(max_length=20,choices=CONTENT_TYPES)
      title = models.CharField(max_length=100, null=True)
      content = models.TextField()
      media = models.FileField(upload_to='post_media',null=True,blank=True)
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
      
      def __str__(self):
            return f"{self.author.email} posted {self.content_type}"
      