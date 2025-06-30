from django.db import models


# Create your models here.
class ChatUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    country_code = models.CharField(max_length=3)
class ChatMessage(models.Model):
    user = models.ForeignKey(ChatUser, on_delete=models.CASCADE)
    message = models.TextField()
    sender = models.BooleanField(default=True)  # True for user
    time_stamp = models.DateTimeField(auto_now_add=True)
