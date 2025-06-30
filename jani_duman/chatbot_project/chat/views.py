from django.shortcuts import render, redirect
from .models import ChatUser, ChatMessage

def chat_view(request):
    if request.method == 'POST':
        message = request.POST.get('message','').strip()
        if not message:
            return redirect('chat')
        # For now, use a test ChatUser
        user, _ = ChatUser.objects.get_or_create(name='Test User', email='test@example.com', phone='1234567890', country_code='+91')
        ChatMessage.objects.create(user=user, message=message, sender=True)
        return redirect('chat')

    messages = ChatMessage.objects.all()
    return render(request, 'chat/chat.html', {'messages': messages})
