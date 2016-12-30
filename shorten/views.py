from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib.auth import authenticate,login
from django.http import Http404, HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import *
from django.contrib import messages
# Create your views here.



def userlogin(request):
    if request.method  == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print(username,password)
        user = authenticate(username=username, password=password)
        if not user:
            return render(request,"home.html",{})
        login(request,user)
        print("user",user.username,"login success")
        return HttpResponseRedirect("/feedurl/")
    return render(request,"home.html",{})
def userregister(request):
    print("!!!!")
    title = "Welcome"
    u = " "
    o = " "
    form= register()
    if request.method  == "POST":
        username = request.POST["username"]
        print(username)
        password = request.POST["password"]
        password1 = request.POST['password1']
        email    = request.POST['email']
        form = register(request.POST)

        print(username,password)
        user = User.objects.filter(username = username)
        user = "apple"
        # if user already there
        # if not user:
        if form.is_valid():
            user = User.objects.create_user(username=username,password=password)

            user = authenticate(username=username, password=password)
            login(request,user)
            print("user",user.username,"register success")
            return HttpResponseRedirect("/feedurl/")
        else:
            return render(request , "register.html",{"title":title,"already":"","ps":"","form":form})

    return render(request , "register.html",{"title":title,"already":u,"ps":o,"form":form})


def feedurl(request):
    if request.user.is_authenticated():
        urls = URL.objects.filter(user = request.user.username)
        print(urls)
        new = {}
        for i in urls:
            a= i.url
            if len(a)>22:
                i.url = a[:22]+"..."


        return render(request , "userurl.html",{"urls":urls})


def addurl(request):
    if request.method == "GET":
        # temp  = URL(user= request.user.username)
        form = inserturl()
        return render(request , "addurl.html",{"form":form})
    else:
        print(request.POST.get("url"),request.POST.get("short"),request.user.username)
        # this select fields reference from
        # https://docs.djangoproject.com/en/1.10/topics/forms/modelforms/
        temp  = URL(user= request.user.username)
        form = inserturl(request.POST,instance = temp)
        print(form.errors.as_data())
        if form.is_valid():
            form.save()
            print(request.user.username,"successful add a url")
            return redirect(feedurl)
        return render(request , "addurl.html",{"form":form})


def user_redirect(request,u,s):
    username = u
    short = s
    users = User.objects.filter(username = username)
    if not users:
        messages = " You are not a user, please register first"
        return render(request , "404.html",{"messages":messages})
    web = URL.objects.filter(user = u, short = s)
    if not web:
        messages = "User does not have such url"
        return render(request , "404.html",{"messages": messages})
    # print(web[0][1])
    return HttpResponseRedirect(web[0].url)


def auto_make_short(request):
    url = "google.com"
