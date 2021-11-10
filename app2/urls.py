from django.urls import path, re_path, include

from app import views


urlpatterns = [
    # re_path("article/(\d{4})/(\d{1,2})", views.article),
    re_path("(\d{4})/(\d{1,2})", views.article),
]
