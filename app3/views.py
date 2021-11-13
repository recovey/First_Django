from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from django.views.decorators.csrf import csrf_protect, csrf_exempt


# @csrf_protect
def index(request):
    # print(request.method)
    # print(request.GET)
    # print(request.META.get("HTTP_HOST"))
    # return HttpResponse("hello world")
    remote_addr = request.META.get("REMOTE_ADDR")
    return render(request,"index.html",{"ip": remote_addr})


def login(request):
    return render(request, "login.html")


@csrf_exempt
def auth(request):
    user = request.POST.get("user")
    pwd = request.POST.get("pwd")
    print(user,pwd)
    if user == "main" and pwd == "123":
        # return HttpResponse("<h1>登录成功</h1>")
        return redirect("/user/")
    # return HttpResponse("<h1>账号或密码错误，请重试</h1>")
    msg = "用户名或密码错误"
    return render(request, "login.html", {"msg": msg})



