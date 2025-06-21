from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status

from .base import ApiTest

User = get_user_model()


class UsersApiTests(ApiTest):
    def test_user_list(self) -> None:
        url = reverse("api_users")
        self.client.login(username="alice", password="password123")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        usernames = [u["username"] for u in response.data]
        self.assertIn("alice", usernames)
        self.assertIn("bob", usernames)
        self.assertIn("carol", usernames)
        self.client.logout()
