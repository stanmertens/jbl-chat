from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status

from .base import ApiTest

User = get_user_model()


class ConversationApiTests(ApiTest):
    def test_conversation_api_requires_auth(self) -> None:
        url = reverse("api_conversations_id", args=[self.user2.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_conversation_api(self) -> None:
        url = reverse("api_conversations_id", args=[self.user2.id])
        self.client.login(username="alice", password="password123")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        bodies = [m["body"] for m in response.data]
        self.assertIn("Hello Bob!", bodies)
        self.assertIn("Hi Alice!", bodies)
        self.assertNotIn("Hey Carol!", bodies)
        self.client.logout()
