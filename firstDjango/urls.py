"""firstDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
# 导入包
from app import views


# from app.views import index, login
# from app2 import views
from django.urls import register_converter


class MobileConverter(object):  # 路由转发器MobileConverter这个名称随便定义，但是regex不能错
    regex = "1[3-9]\d{9}"

    def to_python(self, value):
        print(type(value))
        return value

    def to_url(self, value):
        return value


register_converter(MobileConverter, "mobile")  # 注册一个路由转发器


urlpatterns = [
    # path('admin/', admin.site.urls),
    # path("index/", views.index),
    # path("login/", views.login),
    # path("", views.nulls),
    # re_path("article/(\d{4})/(\d{1,2})", views.article),
    # re_path("article/(\d{4})/(^([1-9]|1[012])$)", views.article)
    # 路由分发
    # path('home/', include('app.urls')),
    # path('article/', include('app2.urls')),
    # path("index/<mobile:mobile>", views.show)
    path("user/", include("app3.urls")),
    # path("login/", include("app3.urls")),
]
