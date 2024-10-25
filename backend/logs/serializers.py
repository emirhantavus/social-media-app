from rest_framework import serializers
from logs.models import IPLog , ActionLog , UserAPIKey

class IPLogSerializers(serializers.ModelSerializer):
      user = serializers.SerializerMethodField()
      class Meta:
            model = IPLog
            fields = ('user','ip_address','last_logged')
            
      def get_user(self,obj):
            return obj.user.email
      
class ActionLogSerializers(serializers.ModelSerializer):
      user_email = serializers.EmailField(source='user.email',read_only=True)
      class Meta:
            model = ActionLog
            fields = ('user_email','action','model_name','object_id','timestamp','detail')
            
class UserAPIKeySerializer(serializers.ModelSerializer):
      class Meta:
            model = UserAPIKey
            fields = ('id','email','api_key','created_at')