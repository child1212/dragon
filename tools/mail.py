
#%%
from time import sleep
import requests
import json


def send_mail(data,host="https://dqa.hphorse.net"):
    url_banding = "{host}/BI/open/sendMail".format(host=host)
    headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "Content-Type": "application/json",
    "Origin": "{host}".format(host=host),
    "Referer": "{host}/BI/open/sendMail".format(host=host)
    }

    res3 = requests.post(url_banding, data, headers=headers)
    res = res3.text
    # res = json.loads(res)
    # res = res["msg"]
    print(res)
    return res

def mails(pid_list,title,content,reward,server):
    data_stand = '{"pid":[],"title":"","content":"","reward":[]}'
    data_json = json.loads(data_stand)
    data_json["pid"] = pid_list
    data_json["title"] = title
    data_json["content"] = content
    data_json["reward"] = reward
    data = json.dumps(data_json)
    res = send_mail(data,server)
    return res

def many_mails(mail_title, mail_content, reward, server, pid_file_path, res_file_path, group_num):
    pid_list = []
    pid_file = open(pid_file_path,"r")
    res_file = open(res_file_path,"w")
    line = pid_file.readline()
    while line:
        pid_list.append(line.replace("\n",""))
        line = pid_file.readline()
        if len(pid_list) == group_num:



            result = mails(pid_list,mail_title,mail_content,reward,server)
            res = json.loads(result)
            if res["code"] == 0:
                for i in eval(res["msg"]):
                    res_file.write(str(i)+"\n")
            else:
                for i in pid_list:
                    res_file.write(i+", fail\n")     
            
            
            # print(pid_list)
            pid_list = []
    # print(pid_list)
    if pid_list:
        result = mails(pid_list,mail_title,mail_content,reward,server)
        res = json.loads(result)
        if res["code"] == 0:
            for i in eval(res["msg"]):
                res_file.write(str(i)+"\n")
        else:
            for i in pid_list:
                res_file.write(i+", fail\n")  
    pid_file.close()
    res_file.close()

#########################################
#邮件标题
mail_title = "Test Mail"
#邮件内容
mail_content = "Dear Adventurers,\n\nThank you for joining us for the grand opening of Fairyscapes Adventure! To celebrate the occasion, we are giving away 50 Free Diamonds every day from June 15th to June 17th. The rewards for each day will be distributed through mail the following day, so don't forget to come back and claim them! We wish you all have a magical experience as you embark on your journey through Fairytale Land!\n\nFairyscapes Adventure Team"
#邮件奖励[[奖励1,数量][奖励2,数量][...,...]]
reward = [[int(input("道具id:")),int(input("道具数量:"))]]
# reward = [[60011,2],[60012,2]]
#玩家id
playerid_list = [input("请输入玩家id:")]
#服务器地址
server = input("请输入服务器地址:")
#########################################

if server == "ntest":
    server = "http://192.168.1.143"
elif server == "nqa":
    server = "https://qa-nfa.hphorse.net"
elif server == "38":
    server = "http://dtest.gameyici.com"
elif server == "qa":
    server = "https://dqa.hphorse.net"
elif server == "act":
    server = "http://dact.gameyici.com"
# elif server == "dragon":
#     server = "https://dragon.hphorse.net"
# elif server == "nrelease":
#     server = "https://online-nfa.hphorse.net"
    
# for i in range(50):
#     result = mails(playerid_list,mail_title,mail_content,reward,server)
while True:    
    result = mails(playerid_list,mail_title,mail_content,reward,server)
    input("continue!")
