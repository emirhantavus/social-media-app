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
  


class RegisterSerializer(serializers.ModelSerializer):
      password = serializers.CharField(write_only=True,required=True,style={'input_type':'password'})
      password2 = serializers.CharField(write_only=True,required=True,style={'input_type':'password'})
      
      class Meta:
            model = get_user_model()
            fields = ['email','password','password2','first_name','last_name']
      
      def validate(self, attrs):
           if attrs['password'] != attrs['password2']:
                 raise serializers.ValidationError({'error':'passwords do not match.'})
           return attrs
      def create(self, validated_data):
            validated_data.pop('password2')
            user = get_user_model().objects.create_user(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
            )
            user.set_password(validated_data['password'])
            user.save()
            return user