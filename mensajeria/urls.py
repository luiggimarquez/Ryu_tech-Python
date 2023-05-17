from django.urls import path
from . import views


urlpatterns = [
    path("", views.usersChat, name="createPage"),
    path("chatRoom/profile:<id>", views.getMessages, name ="chatroom-getmsgs"),
    path("chatRoom/receive", views.sendMessage, name ="chatroom-sendmsgs")      
]

