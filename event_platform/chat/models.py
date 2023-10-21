from django.db import models
from django.conf import settings


class ChatHistory(models.Model):
    text = models.TextField()
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    author = models.CharField(max_length=4, choices=(('ai', 'ai'), ('user', 'user')))
    sent = models.DateTimeField()
