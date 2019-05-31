from flask import Flask, request
import antolib
from linebot import (
    LineBotApi, WebhookHandler,
)
from linebot.exceptions import (
    InvalidSignatureError, LineBotApiError,
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage
)

line_bot_api = LineBotApi('8+wpbLOUtVsyaCZEKB7TUSJLib22ZmYYJ2XcsWD47ZxRr67Dxe/XLKrKDrN0JMd5H3YVveNbL2v1rcwwqIXrkma8cbTJUxOumZe/aTPSYPpf6l0YgqI3/mgnb0fR2gWfkrDzBgXHpbp0yW8R/RvlqgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('4ba0109043212761ae0eb99abbbf28d8')

app = Flask(__name__)

# username of anto.io account
#user = 'YOUR_USERNAME'
# key of permission, generated on control panel anto.io
#key = 'YOUR_KEY'
# your default thing.
#thing = 'YOUR_THING'

#anto = antolib.Anto(user, key, thing)


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
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = event.message.text
    if(message == 'on' or message == 'เปิด'):
        line_bot_api.reply_message(
        event.reply_token,TextSendMessage(text="เปิดสัญญาณกันขโมย"))
    elif(message == 'off' or message == 'ปิด'):
        line_bot_api.reply_message(
        event.reply_token,TextSendMessage(text="ปิดสัญญาณกันขโมย"))
    else:
        line_bot_api.reply_message(
        event.reply_token,TextSendMessage(text="งง"))

if __name__ == "__main__":
#    anto.mqtt.connect()
    app.run(debug=True)
