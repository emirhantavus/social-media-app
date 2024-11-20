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
      
@shared_task
def send_email_welcome(email):
      # send mail for new members
      send_mail(
            subject='Welcome',
            message='You have successfully registered. ',
            from_email='test@gmail.com',
            recipient_list=[email,],
            fail_silently=True
      )