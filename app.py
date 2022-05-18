# SDK(software development kit)

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage,
)

import random

app = Flask(__name__)

# token
line_bot_api = LineBotApi('+vWnf1OreVQHLTrdB854PbdGOqSEuoLa6MBdMA9QRQlNJG1kHxsNNRDQdMnW3NX43s8TQZM+Fo0w+yw/2qn2mZH/eDhuAw3RTs/mRXmLCCbDlwK4kGUK2GiHGVLtiB/tnAKKePzP7sJnmdal+rU+rQdB04t89/1O/w1cDnyilFU=')
# secret
handler = WebhookHandler('66c40ffd229103137640eb68a077c210')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text

    green = ['green1.jpg', 'green2.jpg', 'green3.jpg']
    blue = ['blue1.jpg', 'blue2.jpg', 'blue3.jpg']
    orange = ['orange1.jpg', 'orange2.jpg', 'orange3.jpg']
    purple = ['purple1.jpg', 'purple2.jpg', 'purple3.jpg']
    red = ['red1.jpg', 'red2.jpg', 'red3.jpg']
    random_list = green + blue + orange + purple + red

    if msg in ['hi', 'Hi', '嗨', '']:
        line_bot_api.reply_message(
            event.reply_token,
            StickerSendMessage(
                package_id='1',
                sticker_id='106'
            ))
    elif msg == 'Random':
        ima = random.choice(random_list)
        path = 'https://github.com/bellabula/line-bot/blob/master/Image/' + ima + '?raw=true'
        image_message = ImageSendMessage(
            original_content_url=path,
            preview_image_url=path)
    elif msg == 'green':
        ima = random.choice(green)
        path = 'https://github.com/bellabula/line-bot/blob/master/Image/' + ima + '?raw=true'
        image_message = ImageSendMessage(
            original_content_url=path,
            preview_image_url=path)
    elif msg == 'blue':
        ima = random.choice(blue)
        path = 'https://github.com/bellabula/line-bot/blob/master/Image/' + ima + '?raw=true'
        image_message = ImageSendMessage(
            original_content_url=path,
            preview_image_url=path)
    elif msg == 'orange':
        ima = random.choice(orange)
        path = 'https://github.com/bellabula/line-bot/blob/master/Image/' + ima + '?raw=true'
        image_message = ImageSendMessage(
            original_content_url=path,
            preview_image_url=path)
    elif msg == 'purple':
        ima = random.choice(purple)
        path = 'https://github.com/bellabula/line-bot/blob/master/Image/' + ima + '?raw=true'
        image_message = ImageSendMessage(
            original_content_url=path,
            preview_image_url=path)
    elif msg == 'red':
        ima = random.choice(red)
        path = 'https://github.com/bellabula/line-bot/blob/master/Image/' + ima + '?raw=true'
        image_message = ImageSendMessage(
            original_content_url=path,
            preview_image_url=path)
    else:
        reply = '我無法回答'
        line_bot_api.reply_message(event.reply_token, reply)
    
    line_bot_api.reply_message(event.reply_token, image_message)

if __name__ == "__main__":
    app.run()