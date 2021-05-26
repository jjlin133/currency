from django.conf import settings
from linebot import LineBotApi
from linebot.models import TextSendMessage
import requests
import twder  #匯率套件

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

currencies = {'美金':'USD','港幣':'HKD','英鎊':'GBP','澳幣':'AUD',\
              '日圓':'JPY','歐元':'EUR','人民幣':'CNY' }  #幣別字典
keys = currencies.keys()

def sendUse(event):  #使用說明
    try:
        text1 ='''
查詢匯率：輸入外幣名稱「XXXX」，例如「美金」,「英鎊」,「港幣」,「澳幣」,「日圓」,「歐元」,「人民幣」
               '''
        message = TextSendMessage(
            text = text1
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendTWder_orig(event, mtext):  
    try:
        money = mtext       
        if not money == '':  #匯率類幣別存在
            if money in keys:
                rate_date = twder.now(currencies[money])[0]
                cashBuy = float(twder.now(currencies[money])[1])  #由匯率套件取得匯率
                cashSell = float(twder.now(currencies[money])[2])  #由匯率套件取得匯率
                checkBuy = float(twder.now(currencies[money])[3])  #由匯率套件取得匯率
                checkSell = float(twder.now(currencies[money])[4])  #由匯率套件取得匯率
                message =  rate_date + '\n' + money + '匯率_(台灣銀行端)'+ '\n 現金買入 : ' + str(cashBuy)
                message = message + '\n 現金賣出 : ' + str(cashSell)
                message = message + '\n 即期買入 : ' + str(checkBuy)
                message = message + '\n 即期賣出 : ' + str(checkSell)
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text=message))
            else:
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text=''))
        else:  #其他未知輸入
            text =' 無此幣別匯率資料！，請重新輸入！'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=text))            
    except:
        text = '無法了解你的意思，請重新輸入！'
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=text))
        
        
#函數 sendLUIS 是課本Ch09 範例 >>> 可以修正為自己的函數 sendTWder
def sendTWder(event, mtext):  
    try:
        money = mtext       
        if not money == '':  #匯率類幣別存在
            if mtext == '@使用說明':
                sendUse(event)  
            elif money in keys:
                rate_date = twder.now(currencies[money])[0]
                cashBuy = float(twder.now(currencies[money])[1])  #由匯率套件取得匯率
                cashSell = float(twder.now(currencies[money])[2])  #由匯率套件取得匯率
                checkBuy = float(twder.now(currencies[money])[3])  #由匯率套件取得匯率
                checkSell = float(twder.now(currencies[money])[4])  #由匯率套件取得匯率
                message =  rate_date + '\n' + money + '匯率_(台灣銀行端)'+ '\n 現金買入 : ' + str(cashBuy)
                message = message + '\n 現金賣出 : ' + str(cashSell)
                message = message + '\n 即期買入 : ' + str(checkBuy)
                message = message + '\n 即期賣出 : ' + str(checkSell)
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text=message))
            else:
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text=''))                
        else:  #其他未知輸入
            text =' 其他未知資訊！，請重新輸入！'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=text))            
    except:
        text = '無法了解你的意思，請重新輸入！'
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=text))

################## LIFF　測試網頁　（皆ok,2021.0328） ###################################### 
#北歐福利網頁：https://kknews.cc/zh-tw/world/3q2r8ng.html
#(LIFF)北歐福利網頁 https://liff.line.me/1654001451-WD5802xL

#銘傳網網頁：http://172.104.79.148/mcu/?act=shopping&cmd=main&pg_id=2020093000006

#零存整付試算網 https://currency2021.herokuapp.com/fv2
#(LIFF)零存整付試算   https://liff.line.me/1654001451-0k9NPkVJ

#預約訂房TW行動支付 https://finliff.herokuapp.com/index_form.html
#(LIFF)預約訂房TW行動支付   https://liff.line.me/1654001451-0YAYOpyD

#預約訂房表單網頁(lai帳號) https://hotelformliff.herokuapp.com/index_form.html
#(LIFF_連結至 lai帳號)預約訂房表單   https://liff.line.me/1654001451-zqZ8ewpJ

#(LIFF)北歐福利網頁 https://liff.line.me/1654001451-WD5802xL
#(LIFF)零存整付試算   https://liff.line.me/1654001451-0k9NPkVJ
#(LIFF)預約訂房TW行動支付    https://liff.line.me/1654001451-0YAYOpyD
#(LIFF_連結至 lai帳號)預約訂房表單   https://liff.line.me/1654001451-zqZ8ewpJ
#################################################################################### 

def neuWeb(event):  #網頁連結
    try:
        text1 ='''
北歐福利網頁：https://kknews.cc/zh-tw/world/3q2r8ng.html
銘傳網網頁：http://172.104.79.148/mcu/?act=shopping&cmd=main&pg_id=2020093000006

零存整付試算   https://currency2021.herokuapp.com/fv

歡迎網＆時間　https://currency2021.herokuapp.com/hello4/jenjen/
              '''
        message = TextSendMessage(
            text = text1
#            text = 'https://liff.line.me/1654001451-0YAYOpyD'
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def finWeb(event):  #網頁連結
    try:
        text1 ='''
零存整付試算   https://currency2021.herokuapp.com/fv
              '''
        message = TextSendMessage(
            text = text1
#            text = 'https://liff.line.me/1654001451-0YAYOpyD'
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
        
        
def sendQuickreply(event):  #快速選單
    try:
        message = TextSendMessage(
            text='請選擇最喜歡的程式語言',
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=MessageAction(label="Python", text="Python_Django專案_可建構網頁")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="R", text="R語言_適合進行預測分析與建立預測模型 & RShiny_可建構互動式網頁 ")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="SAS", text="SAS_專業的統計分析軟體")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="SPSS", text="SPSS_社會科學領域的統計分析軟體")
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
