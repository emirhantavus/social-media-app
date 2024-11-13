from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone
from django.conf import settings
from django.contrib.auth import get_user_model

class CustomUserManager(BaseUserManager):
      def create_user(self, email, password=None, **extra_fields):
            if not email:
                  raise ValueError('The Email field must be set')
            email = self.normalize_email(email)
            user = self.model(email=email, **extra_fields)
            if password is None:
                  raise ValueError('Users must have password')
            user.set_password(password)
            user.save(using=self._db)
            return user

      def create_superuser(self, email, password=None, **extra_fields):
            extra_fields.setdefault('is_staff', True)
            extra_fields.setdefault('is_superuser', True)
            extra_fields.setdefault('is_active', True)
            return self.create_user(email, password, **extra_fields)


class Account(AbstractBaseUser,PermissionsMixin):
      email = models.EmailField(unique=True, max_length=255)
      nickname = models.CharField(unique=True,max_length=30, null=True,blank=True)
      first_name = models.CharField(max_length=30, blank=True)
      last_name = models.CharField(max_length=30, blank=True)
      
      is_staff = models.BooleanField(default=False) 
      is_superuser = models.BooleanField(default=False) 
      is_active = models.BooleanField(default=True)
      date_joined = models.DateTimeField(default=timezone.now)
      
      objects = CustomUserManager()
    
      USERNAME_FIELD = 'email'
      
      def __str__(self) -> str:
            return self.email
      
      
class Profile(models.Model):
      user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
      profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
      bio = models.TextField(blank=True)
      date_of_birth = models.DateField(blank=True, null=True)    
       
      def __str__(self):
            return self.user.email
      
      
user = get_user_model()

class Follow(models.Model):
      follower = models.ForeignKey(user, related_name='following', on_delete=models.CASCADE)
      following = models.ForeignKey(user, related_name='followers', on_delete=models.CASCADE)
      created_at = models.DateTimeField(auto_now_add=True)
      

################################## ###################################################
# 5 times Wrong login attempts

class LoginAttempt(models.Model):
      user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True,blank=True)
      ip_address = models.GenericIPAddressField()
      attempts = models.IntegerField(default=0)
      last_attempt = models.DateTimeField(auto_now=True)
      is_blocked = models.BooleanField(default=False)
      blocked_until = models.DateTimeField(null=True,blank=True)
      
      def block(self):
            self.is_blocked = True
            self.blocked_until = timezone.now() + timezone.timedelta(minutes=15) #block 15 mins
            self.save()
            
      def reset_attempts(self):
            self.attempts = 0
            self.is_blocked = False
            self.blocked_until = None
            self.save()