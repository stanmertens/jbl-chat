from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View

User = get_user_model()


@method_decorator(login_required, name="dispatch")
class ChatView(View):
    def get(self, request) -> HttpResponse:
        return render(request, "chat/chat.html")
