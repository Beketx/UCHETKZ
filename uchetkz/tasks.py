from celery import shared_task
from django.core.mail import send_mail
from uchetkz.celery import app


@app.task
def send_beat_email(email):
        send_mail(
            'Task',
            'Your task is done',
            'beketdjango@gmail.com',
            [email],
            fail_silently=False
        )