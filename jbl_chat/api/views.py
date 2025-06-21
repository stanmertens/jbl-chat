from chat.models import Message
from django.contrib.auth import get_user_model
from django.db.models import Q, QuerySet
from rest_framework import generics, permissions
from rest_framework.serializers import BaseSerializer

from .serializers import MessageSerializer, UserSerializer

User = get_user_model()


class UsersAPI(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class ConversationAPI(generics.ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self) -> QuerySet[Message]:
        other_user_id = self.kwargs["user_id"]
        return Message.objects.filter(
            Q(sender=self.request.user, recipient_id=other_user_id)
            | Q(sender_id=other_user_id, recipient=self.request.user)
        ).order_by("timestamp")


class MessageAPI(generics.CreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer: BaseSerializer) -> None:
        serializer.save(sender=self.request.user)
