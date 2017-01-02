"""ShortenUrl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from shorten.views import *
from django.conf.urls.static import static
from django.conf import settings

# import shorten.views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^userregister/',userregister ,name = "reg" ),
    url(r'^feedurl/',feedurl ,name = "feedurl" ),
    url(r'^$', userlogin, name= "userlogin"),

    url(r'addurl/',addurl, name= "addurl"),
    url(r'editurl/',editurl, name= "editurl"),
    url(r'removeurl/',removeurl, name= "removeurl"),
    url(r'(.*)/(.*)',user_redirect,name= "user_redirect"),




] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
