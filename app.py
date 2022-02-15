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

    if msg in ['hi', 'Hi']:
        line_bot_api.reply_message(
            event.reply_token,
            StickerSendMessage(
                package_id='106',
                sticker_id='1'
            ))
    elif msg == '你是誰':
        reply = "我是機器人"
    elif "time" in msg:
        reply = "營業時間:一~五, 0900-1700"
    else:
        reply = '我無法回答'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply))

if __name__ == "__main__":
    app.run()