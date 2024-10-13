from rest_framework import serializers
from logs.models import IPLog

class IPLogSerializers(serializers.ModelSerializer):
      user = serializers.SerializerMethodField()
      class Meta:
            model = IPLog
            fields = ('user','ip_address','last_logged')
            
      def get_user(self,obj):
            return obj.user.email