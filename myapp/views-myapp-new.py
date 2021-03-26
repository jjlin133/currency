from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

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
   return render(request,"hello4.html",locals()) 