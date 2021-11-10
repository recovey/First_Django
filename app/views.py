import datetime

from django.shortcuts import render, HttpResponse
from time import time
# Create your views here.


def index(request):
    # 返回一个字符串
    # return HttpResponse("主页")
    # 返回一个静态页面
    return render(request, "index.html")


def login(request):
    return HttpResponse("登录页面")


def nulls(request):
    nowtime = datetime.datetime.now().strftime("%Y-%m-%d %X")
    return render(request, "time/time.html", {"now": nowtime})
    # return HttpResponse("默认路径")


def article(request, year, month):
    print(year)
    print(month)
    return HttpResponse("现在是：%s年 %s月" % (year, month))


def show(request,mobile):
    print(mobile,type(mobile))
    return HttpResponse(f"hi,{mobile}用户")