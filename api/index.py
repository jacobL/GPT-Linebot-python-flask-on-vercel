from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, FlexSendMessage
from api.chatgpt import ChatGPT
from api.flex_message_template import get_flex_message_content
import json
import os
import uuid

line_bot_api = LineBotApi(os.getenv("LINE_CHANNEL_ACCESS_TOKEN"))
line_handler = WebhookHandler(os.getenv("LINE_CHANNEL_SECRET"))
working_status = os.getenv("DEFALUT_TALKING", default = "true").lower() == "true"

app = Flask(__name__)
chatgpt = ChatGPT()
CACHE = {} #付款用

# domain root
@app.route('/')
def home():
    return 'Hello, World!'

@app.route("/webhook", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        line_handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

def pay():
    product_name = 'AI敏捷專家Line諮詢(1小時)'
    price = 99
    order_id = str(uuid.uuid4())
    amount = 1
    currency = "TWD"
    CACHE["order_id"] = order_id
    CACHE["amount"] = amount
    CACHE["currency"] = currency
    #-------------設定flex message----------------------------------
    print(str(event)) 
    #tmp_obj = json.loads(str(event.source))
    #line_id = str(tmp_obj['userId'])
    line_id = json.loads(str(event.source))['userId']
    profile = line_bot_api.get_profile(line_id) # 取得line名稱
    
    flex_content = get_flex_message_content(profile.display_name, order_id) # 設定flexmessage模板
    #---------------------------------------------------------------
    line_bot_api.push_message(line_id, FlexSendMessage(
                        alt_text='hello',
                        contents=flex_content
                    ))
    
@line_handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    global working_status
    if event.message.type != "text":
        return
    
    if event.message.text == "說話":
        working_status = True
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="我可以說話囉，歡迎來跟我互動 ^_^ "))
        return
    if event.message.text == "pay":
        pay()       
        return
        
    if event.message.text == "閉嘴":
        working_status = False
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="好的，我乖乖閉嘴 > <，如果想要我繼續說話，請跟我說 「說話」 > <"))
        return

    if working_status:
        chatgpt.add_msg(f"HUMAN:{event.message.text}?\n")
        reply_msg = chatgpt.get_response().replace("AI:", "", 1)
        chatgpt.add_msg(f"AI:{reply_msg}\n")
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=reply_msg))


if __name__ == "__main__":
    app.run()
