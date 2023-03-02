import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restApicrashcourse.settings')

app = Celery('restApicrashcourse')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print("Hello from celery")


@app.task
def print_hello():
    print("Hello from function")



@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')



from django.core.mail import send_mail
from django.conf import settings
from decouple import config

@app.task
def send_mail_task():

    send_mail("CELERY WORKED YEAH!",
        "CELERY IS COOL",
        config('EMAIL_HOST_USER'),
        ['techwithsns@gmail.com'],
        fail_silently = False
    )
    print("Email Send")