from api.serializers import MessageSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.utils.decorators import method_decorator
from django.views import View
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from chat.models import Message

User = get_user_model()


class MessageHTMX(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request: HttpRequest) -> Response:
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            message = serializer.save(sender=request.user)
            html = render(request, "chat/_message.html", {"message": message})
            return HttpResponse(html, content_type="text/html")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(login_required, name="dispatch")
class MessagesHTMX(View):
    def get(self, request: HttpRequest, user_id: int) -> HttpResponse:
        other_user = get_object_or_404(User, id=user_id)
        messages = Message.objects.filter(
            Q(sender=request.user, recipient=other_user)
            | Q(sender=other_user, recipient=request.user)
        ).order_by("timestamp")
        html = render(request, "chat/_messages.html", {"messages": messages})
        return HttpResponse(html, content_type="text/html")


@method_decorator(login_required, name="dispatch")
class ConversationHTMX(View):
    def get(self, request: HttpRequest, user_id: int) -> HttpResponse:
        other_user = get_object_or_404(User, id=user_id)
        html = render(request, "chat/_conversation.html", {"other_user": other_user})
        return HttpResponse(html, content_type="text/html")


@method_decorator(login_required, name="dispatch")
class UsersHTMX(View):
    def get(self, request: HttpRequest, user_id: int) -> HttpResponse:
        users = User.objects.exclude(id=request.user.id)
        html = render(request, "chat/_users.html", {"users": users})
        return HttpResponse(html, content_type="text/html")
