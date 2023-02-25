from celery import shared_task
from time import sleep




@shared_task
def sleepy(duration):
    sleep(duration)
    return None


from django.core.mail import send_mail
from django.conf import settings
from decouple import config

@shared_task
def send_mail_task():

    send_mail("CELERY WORKED YEAH!",
        "CELERY IS COOL",
        config('EMAIL_HOST_USER'),
        ['shoaibbilal101@gmail.com'],
        fail_silently = False
    )
    return None