from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone

class CustomUserManager(BaseUserManager):
      def create_user(self, email, password=None, **extra_fields):
            if not email:
                  raise ValueError('The Email field must be set')
            email = self.normalize_email(email)
            user = self.model(email=email, **extra_fields)
            if password:
                  user.set_password(password)
            else:
                  raise ValueError('Users must have password')
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
      profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
      bio = models.TextField(blank=True)
      date_of_birth = models.DateField(blank=True, null=True)
      followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)
      
      is_active = models.BooleanField(default=True)
      date_joined = models.DateTimeField(default=timezone.now)
      
      objects = CustomUserManager()
    
      USERNAME_FIELD = 'email'
      
      def __str__(self) -> str:
            return self.email