from comments.models import Comment
from notifications.utils import create_notification

def post_comment(user, post, comment_text):
      comment = Comment.objects.create(author=user, post=post, content=comment_text)
      
      create_notification(
            user=post.author,
            message=f"{user.email} commented on your post: {post.title}"
      )
      
      return comment