from django.urls import path

from .views import ConversationAPI, MessageAPI, UsersAPI

urlpatterns = [
    path(
        "users/",
        UsersAPI.as_view(),
        name="api_users",
    ),
    path(
        "conversations/<int:user_id>/",
        ConversationAPI.as_view(),
        name="api_conversations_id",
    ),
    path(
        "messages/",
        MessageAPI.as_view(),
        name="api_messages",
    ),
]
