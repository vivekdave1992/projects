from django.contrib import admin
from .models import ChatMessage, ChatUser
# Register your models here.
admin.site.register(ChatUser)
admin.site.register(ChatMessage)
