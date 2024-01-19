import time
from time import sleep
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util import Retry
from datetime import datetime
from utils.mydate import getMonday, formatDate, formatSeconds
from atcoder import get_atcoder_contests
from newcoder import get_nowcoder_contests

url_reboot = "http://127.0.0.1:5700"
url_cf = "http://codeforces.com/api"

RES = requests.session()
RES.mount('http://', HTTPAdapter(max_retries=Retry(total=5)))
RES.mount('https://', HTTPAdapter(max_retries=Retry(total=5)))

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'
}

# 获取即将开始的比赛信息
def getContests():
    response = RES.get(url=url_cf + "/contest.list")
    while response.status_code != 200:
        response = RES.get(url=url_cf + "/contest.list")
        sleep(0.3)
    res = response.json().get("result")
    contests = []
    for i in res:
        if i.get("phase") == "FINISHED":
            break
        contest = {
            "name": i.get("name"),
            "begin_time": formatDate(i.get("startTimeSeconds")),
            "end_time": formatDate(i.get("startTimeSeconds") + i.get("durationSeconds")),
            "type": i.get("type"),
            "status": i.get("phase"),
            "relative_time": i.get("relativeTimeSeconds"),
            "id":i.get("id"),
        }
        reset = abs(i.get("relativeTimeSeconds"))
        if reset > 7*24*60*60 :
            continue
        contests.append(contest)
    message = "《Codeforces 比赛日历》\n "
    if len(contests) == 0:
        message += "[空空如也]\t\t\n\n"
        return message
    for i in contests[::-1]:
        message += " 	比赛名称 : " + i["name"] + "     \n" \
                    + " 	比赛链接： https://codeforces.com/contestRegistration/" + str(i["id"]) + "     \t\n" \
                   + " 	开始时间 : " + i["begin_time"] + "     \t\n" \
                   + " 	结束时间 : " + i["end_time"] + "     \t\n" \
                   + " 	比赛类型 : " + i["type"] + "     \t\n"
        if i["status"] != "BEFORE":
            message += " 	比赛状态 : 进行中...\t\n\n"
        else:
            message += " 	比赛状态 : 未开始，距开始剩余 " + formatSeconds(abs(i["relative_time"])) + "\t\n\n"
    now_time = datetime.now()
    now_time = datetime.strftime(now_time, '%Y-%m-%d %H:%M:%S')
    message = message + "更新时间 : " + now_time
    return message

# 发送比赛日历至 QQ 群
def sendGroupContests(group_id, nickname,u_id=None, flag=True):
    if not flag:
        pass
    data = {
        "group_id": group_id,
        "message":  getContests()
    }
    requests.post(url=url_reboot + "/send_group_msg", json=data)


# 发送比赛日历（私聊）
def sendPrivateContests(uid):
    message = getContests()
    data = {
        "user_id": uid,
        "message": message
    }
    requests.post(url=url_reboot + "/send_private_msg", json=data)

def sendPrivateAtcoderContests(uid,nickname):
    contests = get_atcoder_contests()
    message = "《Atcoder比赛日历》\n"
    for x in contests:
        contest_time = list(map(str, x['contest_time']))
        message = message + " 	比赛名字：\t" + x['name'] + "\n" + " 	比赛链接：\t" + x['link'] + "\n" + " 	比赛时间：\t" + \
                  contest_time[0] + "至" + contest_time[1] + "\n\n"
    now_time = datetime.now()
    now_time = datetime.strftime(now_time, '%Y-%m-%d %H:%M:%S')
    message = message + "更新时间 : " + now_time
    data = {
        "user_id":uid,
        "message":message
    }
    requests.post(url=url_reboot + "/send_private_msg", json=data)

def sendGroupAtcoderContests(group_id,uid,nickname):
    contests = get_atcoder_contests()
    message = "《Atcoder比赛日历》\n"
    for x in contests:
        contest_time = list(map(str, x['contest_time']))
        message = message + " 	比赛名字：\t" + x['name'] + "\n" + " 	比赛链接：\t" + x['link'] + "\n" + " 	比赛时间：\t" + contest_time[0] + "至" + contest_time[1] + "\n\n"
    now_time = datetime.now()
    now_time = datetime.strftime(now_time, '%Y-%m-%d %H:%M:%S')
    message = message + "更新时间 : " + now_time
    data = {
        "group_id": group_id,
        "message": message
    }
    requests.post(url=url_reboot + "/send_group_msg", json=data)

def sendPrivateNowCoderContests(uid,nickname):
    contests = get_nowcoder_contests()
    message = "《牛客比赛日历》\n"
    for x in contests:
        contest_time = list(map(str, x['contest_time']))
        message = message + " 	比赛名字：\t" + x['name'] + "\n" + " 	比赛链接：\t" + x['link'] + "\n" + " 	比赛时间：\t" + \
                  contest_time[0] + "至" + contest_time[1] + "\n\n"
    now_time = datetime.now()
    now_time = datetime.strftime(now_time, '%Y-%m-%d %H:%M:%S')
    message = message + "更新时间 : " + now_time
    data = {
        "user_id":uid,
        "message":message
    }
    requests.post(url=url_reboot + "/send_private_msg", json=data)

def sendGroupNowCoderContests(group_id,uid,nickname):
    contests = get_nowcoder_contests()
    print(contests)
    message = "《牛客比赛日历》\n"
    for x in contests:
        contest_time = list(map(str, x['contest_time']))
        message = message + " 	比赛名字：\t" + x['name'] + "\n" + " 	比赛链接：\t" + x['link'] + "\n" + " 	比赛时间：\t" + \
                  contest_time[0] + "至" + contest_time[1] + "\n\n"
    now_time = datetime.now()
    now_time = datetime.strftime(now_time, '%Y-%m-%d %H:%M:%S')
    message = message + "更新时间 : " + now_time
    data = {
        "group_id": group_id,
        "message": message
    }
    requests.post(url=url_reboot + "/send_group_msg", json=data)
