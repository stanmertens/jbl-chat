from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status

from .base import ApiTest

User = get_user_model()


class MessagesApiTests(ApiTest):
    def test_message_list_requires_auth(self) -> None:
        url = reverse("api_messages")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_message_list(self) -> None:
        url = reverse("api_messages")
        self.client.login(username="alice", password="password123")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.client.logout()

    def test_create_message_requires_auth(self) -> None:
        url = reverse("api_messages")
        data = {"recipient": self.user2.id, "body": "Test message"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_message(self) -> None:
        url = reverse("api_messages")
        self.client.login(username="alice", password="password123")
        data = {"recipient": self.user2.id, "body": "New message!"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["body"], "New message!")
        self.assertEqual(response.data["recipient"], self.user2.id)
        self.assertEqual(response.data["sender"]["id"], self.user1.id)
        self.client.logout()
