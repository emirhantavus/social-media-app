from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_email_notification(email, subject, message):
      # send mail for notifications
      send_mail(
            subject=subject,
            message=message,
            from_email="test@mail.com",
            recipient_list=[email],
            fail_silently=False
      )