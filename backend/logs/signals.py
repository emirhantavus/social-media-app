from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from logs.models import ActionLog
from movies.models import Movie
from django.contrib.auth import get_user_model
from django_currentuser.middleware import get_current_authenticated_user

user = get_user_model()

@receiver(post_save, sender=Movie)
def log_movie_save(sender, instance, created, **kwargs):
      user = get_current_authenticated_user()
      if user and user.is_authenticated:
            action = 'CREATE' if created else 'UPDATE'
            ActionLog.objects.create(
                  user=user,
                  action=action,
                  model_name='Movie',
                  object_id=instance.id,
                  detail=f"Movie '{instance.title}' has been {'created' if created else 'updated'}."
            )
            
            
            
@receiver(post_delete, sender=Movie)
def log_movie_delete(sender, instance, **kwargs):
    user = get_current_authenticated_user()
    if user and user.is_authenticated:
        ActionLog.objects.create(
            user=user,
            action='DELETE',
            model_name='Movie',
            object_id=instance.id,
            detail=f"Movie '{instance.title}' has been deleted."
        )