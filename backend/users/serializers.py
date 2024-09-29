from rest_framework import serializers
from users.models import Account , Profile , Follow
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(serializers.ModelSerializer):
      followers_count = serializers.SerializerMethodField()
      following_count = serializers.SerializerMethodField()
      
      class Meta:
            model = get_user_model()
            fields = ['id', 'email', 'nickname', 'first_name', 'last_name','followers_count', 'following_count']
            
      def get_followers_count(self,obj):
            return obj.followers.count()
      
      def get_following_count(self, obj):
        return obj.following.count()
  


class RegisterSerializer(serializers.ModelSerializer):
      password = serializers.CharField(write_only=True,required=True,style={'input_type':'password'})
      password2 = serializers.CharField(write_only=True,required=True,style={'input_type':'password'})
      
      class Meta:
            model = get_user_model()
            fields = ['email','password','password2','first_name','last_name','nickname']
      
      def validate(self, attrs):
           if attrs['password'] != attrs['password2']:
                 raise serializers.ValidationError({'error':'passwords do not match.'})
           return attrs
     
      def create(self, validated_data):
            validated_data.pop('password2')
            user = get_user_model().objects.create_user(
                  email=validated_data['email'],
                  first_name=validated_data['first_name'],
                  last_name=validated_data['last_name'],
                  nickname=validated_data.get('nickname'),
                  password=validated_data['password']
                  )
            user.set_password(validated_data['password'])
            user.save()
            Profile.objects.get_or_create(user=user)
            return user
      
class ProfileUpdateSerializer(serializers.ModelSerializer):
      
      class Meta:
            model = Profile
            fields = ['profile_photo','bio','date_of_birth',]
            
      def validate_nickname(self,value):
            user = self.context['request'].user
            if Account.objects.exclude(id=user.id).filter(nickname=value).exists():
                  raise serializers.ValidationError('this nickname is already in use')
            return value
      
      def update(self, instance, validated_data):
            instance.profile_photo = validated_data.get('profile_photo', instance.profile_photo)
            instance.bio = validated_data.get('bio', instance.bio)
            instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
            instance.save()
            return instance
      
      
class LoginSerializer(serializers.Serializer):
      email = serializers.EmailField(required=True)
      password = serializers.CharField(required=True,write_only=True,style={'input_type':'password'})
      
class FollowSerializer(serializers.Serializer):
      class Meta:
            model = Follow
            fields = ['follower', 'following']
      
      def create(self, validated_data):
            follow_instance = Follow.objects.create(**validated_data)
            return follow_instance