from flask import Flask, request
from methods import sendPrivateContests, sendGroupContests,\
    sendGroupAtcoderContests,sendGroupNowCoderContests,sendPrivateNowCoderContests,sendPrivateAtcoderContests

app = Flask(__name__)

qqnumber = "3392562158" #填写登陆qq号的账号，以便后期@使用，防止消息误触

@app.route('/', methods=["POST"])
def post_data():
    if request.get_json().get("message_type") == "private":  # 如果是私聊信息
        uid = request.get_json().get('sender').get('user_id')  # 获取信息发送者的 QQ号码
        nickname = request.get_json().get("sender").get("nickname")
        message = request.get_json().get('raw_message')  # 获取原始信息
        if message == "atcoder -c" or message == "at -c":
            print(uid, nickname, message)
            sendPrivateAtcoderContests(uid,nickname)
        if message == "nowcoder -c" or message == "nk -c":
            print(uid, nickname, message)
            sendPrivateNowCoderContests(uid, nickname)
        if message == "cf -c" or message == "cf contests":
            print(uid, nickname, message)
            sendPrivateContests(uid)

    if request.get_json().get('message_type') == 'group':  # 如果是群聊信息
        gid = request.get_json().get('group_id')  # 获取群号
        uid = request.get_json().get('sender').get('user_id')  # 获取信息发送者的 QQ号码
        nickname = request.get_json().get("sender").get("nickname")
        message = request.get_json().get('raw_message')  # 获取原始信息
        if "[CQ:at,qq="+qqnumber+"]" in message:
            if "atcoder -c" in message or "at -c" in message:
                print(uid, nickname, message)
                sendGroupAtcoderContests(gid,uid,nickname)
            if "nowcoder -c" in message or "nk -c" in message:
                print(uid, nickname, message)
                sendGroupNowCoderContests(gid,uid,nickname)
            if "cf -c" in message or "cf contests" in message:
                print(uid, nickname, message)
                sendGroupContests(gid, nickname,uid)
    return "OK"

if __name__ == '__main__':
    target=app.run(debug=True, host='127.0.0.1', port=5705)

