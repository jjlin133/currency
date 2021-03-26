from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# 增加 ~~~
from django.conf import settings
from linebot.models import *

# Create your views here.
# define sayhello
def sayhello(request):
   return HttpResponse("Hello Django!")


# define hello3
def hello3(request,username):
   now=datetime.now()
   return render(request,"hello3.html",locals())
   
# define hello4
def hello4(request,username):
   now=datetime.now()
   username="Jen-Jen Lin @2021.0320"
   return render(request,"hello4.html",locals()) 

# define fv
def fv(request):
   return render(request,"E_8_1_orig.html",locals()) 
   
# define fv2
def fv2(request):
   return render(request,"E_8_1.html",locals()) 
