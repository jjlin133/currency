from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# 增加 ~~~
from django.conf import settings
from linebot.models import *

##########################################
# add the follows from linebotLUIS\luisapi\views.py
from django.http import  HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent
from module import func

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)
#########################################################
@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):
                mtext = event.message.text
                if mtext=='@匯率查詢說明':  #LINE Bot 專案 currency_Demo ### mtext=='@查詢說明' --- LINE Bot 專案 currency
                    func.sendUse(event)
                elif mtext=='@北歐貿易':  # --- LINE Bot 專案 currency
                    func.neuWeb(event)
                elif mtext=='@理財試算':  # --- LINE Bot 專案 currency
                    func.neuWeb(event)
                elif mtext=='@程式語言選單':  #LINE Bot 專案 currency_Demo --- 多項選單
                    func.sendQuickreply(event)

                else:  #一般性輸入
                    func.sendTWder(event, mtext)

        return HttpResponse()
    else:
        return HttpResponseBadRequest()

########################################################

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
