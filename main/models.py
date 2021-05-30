from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateTimeField()
    status = models.BooleanField(default=False)
    user = models.ForeignKey('userauth.CustomUser', on_delete=models.CASCADE)