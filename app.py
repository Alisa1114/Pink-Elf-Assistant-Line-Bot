from flask import Flask, abort, request
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('z/RsFlHM/rjFDSh/0GfTGCOr/Lwn7Jlg4vVv2htG3EtUghvq5hiH67LfMW083g1FK48m+UJeLRcOVd97Rty7zRIGd8Uy7cq6gwTLUv/BQ8KfXJ5qCxQophKJm2nCHx0unpLAJ8YEMxuAyJB1GbAgaQdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('b5e018cb86b24240d7bab68e6ba8f54a')

# 監聽所有來自 /callback 的 Post Request
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

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message)

import os

if __name__ == "__main__":
    print('Hi~')
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)