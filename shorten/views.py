from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib.auth import authenticate,login
from django.http import Http404, HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import *
from django.contrib import messages
from shorturl import *
# Create your views here.



def userlogin(request):
    form = login_form()
    if request.method  == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print(username,password)
        user = authenticate(username=username, password=password)
        if not user:
            return render(request,"home.html",{"form":form,"error":"User Does not exist Or Wrong password"})
        login(request,user)
        print("user",user.username,"login success")
        return HttpResponseRedirect("/feedurl/")

    return render(request,"home.html",{"form":form})
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
        # print(urls)
        # new = {}
        # for i in urls:
        #     a= i.url
        #     if len(a)>22:
        #         i.url = a[:22]+"..."

        return render(request , "userurl.html",{"urls":urls})


def addurl(request):
    if request.method == "GET":
        # temp  = URL(user= request.user.username)
        form = inserturl(user = request.user)
        return render(request , "addurl.html",{"form":form})
    else:
        print(request.POST.get("url"),request.POST.get("short"),request.user.username)
        # this select fields reference from
        # https://docs.djangoproject.com/en/1.10/topics/forms/modelforms/
        temp  = URL(user= request.user.username)
        form = inserturl(request.POST,instance = temp,user = request.user)
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



def editurl(request):
    if request.method == "GET":
        url = request.GET["url"]
        short = request.GET["short"]
        print(url,short)
        print("before remove",len(URL.objects.all()))
        temp = URL(user = request.user.username)
        temp.url = url
        temp.short = short
        temp = URL.objects.get(user = request.user.username,short = short)
        temp.delete()
        form = inserturl(initial = {"user":request.user.username , "url" :url ,  "short":short})
        print(form)
        print("after remove",len(URL.objects.all()))
        return render(request , "editurl.html",{"url":url,"short":short,"form":form})
    else:
        temp  = URL(user= request.user.username)
        form = inserturl(request.POST,instance = temp,user = request.user)
        print("the form looks like",form)
        if form.is_valid():
            print("the form is alid")
            form.save()
            return redirect(feedurl)

def removeurl(request):
    short = request.GET["short"]
    temp = URL.objects.get(user = request.user.username,short = short)
    temp.delete()
    return redirect(feedurl)


def about(request):
    return render(request , "about.html",{})


def auto_url(request):
    if request.method == "GET":
        return render(request , "auto_url.html",{})
    else:
        a= len(URL.objects.all())+1

        ans = Shorten_encode(a)
        result = "https://rocky-reef-93048.herokuapp.com/"+request.user.username+"/"+ans

        return render(request , "auto_url.html",{"result":ans})
