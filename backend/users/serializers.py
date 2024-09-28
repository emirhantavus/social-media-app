from rest_framework import serializers
from users.models import Account
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(serializers.ModelSerializer):
      followers_count = serializers.SerializerMethodField()
      following_count = serializers.SerializerMethodField()
      
      class Meta:
            model = get_user_model()
            fields = ['id', 'email', 'nickname', 'first_name', 'last_name', 'profile_photo', 'bio', 'date_of_birth', 'followers_count', 'following_count']
            
      def get_followers_count(self,obj):
            return obj.followers.count()
      
      def get_following_count(self, obj):
        return obj.following.count()