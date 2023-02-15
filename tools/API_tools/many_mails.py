
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
mail_title = "Compensation Mail"
mail_content = "Dear players, we are sorry for the problem during the repair of Dragon's Nest, this problem has been fixed now, this is some of our thoughts, please check it"
reward = [[101001,2],[102001,2],[103001,2],[104001,2],[105001,2],[106001,2],[107001,2],[108001,2],[109001,2],[110001,2],[111001,2],[201001,2],[202001,2],[203001,2],[204001,2],[205001,2],[206001,2],[207001,2],[301001,2],[302001,2],[303001,2],[401001,2],[402001,2],[403001,2],[404001,2],[2020,9000],[2021,9000],[2022,9000],[2023,9000]]
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


many_mails(mail_title, mail_content, reward, server, pid_file_path, res_file_path, group_num)

# %%
for num in (101,102,103,104,105,106,107,108,109,110,111,201,202,203,204,205,206,207,301,302,303,401,402,403,404,):
    print('[{num}001,2],'.format(num=num),end='')
for num in range(2020,2024):
    print('[{num},9000],'.format(num=num),end='')
# %%
