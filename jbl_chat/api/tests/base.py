from chat.models import Message
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase

User = get_user_model()


class ApiTest(APITestCase):
    def setUp(self) -> None:
        self.user1 = User.objects.create_user(username="alice", password="password123")
        self.user2 = User.objects.create_user(username="bob", password="password123")
        self.user3 = User.objects.create_user(username="carol", password="password123")
        self.message1 = Message.objects.create(
            sender=self.user1,
            recipient=self.user2,
            body="Hello Bob!",
        )
        self.message2 = Message.objects.create(
            sender=self.user2,
            recipient=self.user1,
            body="Hi Alice!",
        )
        self.message3 = Message.objects.create(
            sender=self.user1,
            recipient=self.user3,
            body="Hey Carol!",
        )
