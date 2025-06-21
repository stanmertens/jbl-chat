from django.urls import path

from .views.htmx import ConversationHTMX, MessageHTMX, MessagesHTMX, UsersHTMX
from .views.pages import ChatView

urlpatterns = [
    path(
        "",
        ChatView.as_view(),
        name="chat",
    ),
    path(
        "htmx/message/",
        MessageHTMX.as_view(),
        name="htmx_message",
    ),
    path(
        "htmx/messages/<int:user_id>/",
        MessagesHTMX.as_view(),
        name="htmx_messages_id",
    ),
    path(
        "htmx/conversations/<int:user_id>/",
        ConversationHTMX.as_view(),
        name="htmx_conversations_id",
    ),
    path(
        "htmx/users/<int:user_id>/",
        UsersHTMX.as_view(),
        name="htmx_users_id",
    ),
]
