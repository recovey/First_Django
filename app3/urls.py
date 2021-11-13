from django.urls import path

from app3 import views

urlpatterns = [
    path("", views.index),
    path("login", views.login),
    path("auth", views.auth),
]
