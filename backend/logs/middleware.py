from .models import IPLog
from django.utils import timezone

class LogIPMiddleware:
      def __init__(self, get_response):
            self.get_response = get_response

      def __call__(self, request):
            ip_address = request.META.get('REMOTE_ADDR')

            if request.user.is_authenticated:
                  user = request.user
                  ip_log, created = IPLog.objects.get_or_create(user=user, ip_address=ip_address)
                  if created: # yeni kayıt olursa logla..!! sonra değiştiricem kalsın burda.
                        ip_log.last_logged = timezone.now()
                        ip_log.save()

            response = self.get_response(request)
            return response
