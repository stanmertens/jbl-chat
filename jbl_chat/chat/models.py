from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    image_url = models.URLField(blank=True, null=True)


class Message(models.Model):
    sender = models.ForeignKey(
        User,
        related_name="sent_messages",
        on_delete=models.CASCADE,
    )
    recipient = models.ForeignKey(
        User,
        related_name="received_messages",
        on_delete=models.CASCADE,
    )
    body = models.TextField(null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["timestamp"]

    def __str__(self) -> str:
        return f"{self.timestamp:%Y-%m-%d %H:%M} | {self.sender} -> {self.recipient}"
