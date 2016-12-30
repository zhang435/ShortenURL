from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django import forms
class URL(models.Model):
    user = models.CharField(max_length = 30,blank = True  ,null  = True)
    short = models.CharField(max_length = 30,blank = False,null  = False)
    url   = models.CharField(max_length = 200,blank = False,null  = False)


    def __unicode__(self):
        return self.user+"     "+self.short+"       "+self.url
