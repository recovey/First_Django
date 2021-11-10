from django.contrib import admin
from django.urls import path, re_path, include
# 导入包
from app import views
# from app.views import index, login
# from app2 import views


urlpatterns = [
    path("index/", views.index),
    path("login/", views.login),
    path("", views.nulls),
]