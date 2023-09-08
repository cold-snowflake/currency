from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def debug():
    from time import sleep
    sleep(10)
    print('DEBUG\n' * 10)


@shared_task
def send_email_to_background(subject, message):
    from time import sleep
    recipient = settings.EMAIL_HOST_USER
    sleep(20)
    send_mail(
        subject,
        message,
        recipient,
        [recipient],
        fail_silently=False
    )
