from django.shortcuts import render, HttpResponse

# Create your views here.


def article(request, year, month):
    print(year)
    print(month)
    return HttpResponse("现在是：%s年 %s月" % (year, month))
