from django.urls import path, include
from chat import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path("", views.chatPage, name="chat-page"),
    # login-section
    path("auth/login/", LoginView.as_view
         (template_name="chat/room.html"), name="login-user"),
    path("auth/logout/", LogoutView.as_view(), name="logout-user"),
]
