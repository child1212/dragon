
#%%
from time import sleep
import requests
import json
import time

expList = []
expfile = open("D:\\pyprogram\\PyTestTools\\dragon\\tools\\API_tools\\exp.txt","r",encoding="utf-8-sig")
for line in expfile:
    line=line.replace("\n","")
    a=line.split(",")
    expList.append(a)
expfile.close()


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
mail_content = time.asctime(time.localtime())
server = "ntest" 
group_num = 10
pid_file_path = "PidListExp.txt"
res_file_path = "result_list.txt"

#########################################

if server == "ntest":
    server = "https://nfa-test.bettagames.com"
elif server == "nqa":
    server = "https://qa-nfa.hphorse.net"
# elif server == "nrelease":
#     server = "https://online-nfa.hphorse.net"
elif server == "38":
    server = "http://dtest.gameyici.com"
elif server == "qa":
    server = "https://dqa.hphorse.net"
# elif server == "dragon":
#     server = "https://dragon.hphorse.net"
elif server == "act":
    server = "http://dact.gameyici.com"


for data_list in expList:
    mail_title = "等级:{level}".format(level=data_list[0])
    reward = [[1000,int(data_list[1])]]

    many_mails(mail_title, mail_content, reward, server, pid_file_path, res_file_path, group_num)

# %%
