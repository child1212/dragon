
#%%
from time import sleep
from py import code
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
mail_title = "Activity map compensation"
mail_content = "Dear player, this is the compensation for your reward, please check it"
reward = [[20008,1]]
server = "ntest"
group_num = 10
pid_file_path = "pid_list.txt"
res_file_path = "result_list.txt"

#########################################

if server == "ntest":
    server = "https://nfa-test.bettagames.com"
elif server == "nqa":
    server = "https://qa-nfa.hphorse.net"
elif server == "nrelease":
    server = "https://online-nfa.hphorse.net"
elif server == "38":
    server = "http://dtest.gameyici.com"
elif server == "qa":
    server = "https://dqa.hphorse.net"
elif server == "dragon":
    server = "https://dragon.hphorse.net"
elif server == "act":
    server = "http://dact.gameyici.com"
    
rewards = [[[101001, 1]], [[102001, 1]], [[103001, 1]], [[104001, 1]], [[105001, 1]], [[106001, 1]], [[107001, 1]], [[108001, 1]], [[109001, 1]], [[110001, 1]], [[111001, 1]], [[112001, 1]], [[201001, 1]], [[202001, 1]], [[203001, 1]], [[204001, 1]], [[205001, 1]], [[206001, 1]], [[207001, 1]], [[301001, 1]], [[302001, 1]], [[303001, 1]], [[304001, 1]], [[401001, 1]], [[402001, 1]], [[403001, 1]], [[404001, 1]], [[405001, 1]], [[406001, 1]], [[407001, 1]], [[408001, 1]]]
for reward in rewards:
    many_mails(mail_title, mail_content, reward, server, pid_file_path, res_file_path, group_num)


