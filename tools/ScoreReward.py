from time import sleep
import os
pack_pos = os.path.dirname(os.path.dirname(__file__))
import sys
sys.path.append('{pack_pos}\\function'.format(pack_pos=pack_pos))
sys.path.append('{pack_pos}\\package'.format(pack_pos=pack_pos))
import requests
import json
from xieyi import *
from func_dragon import *
import pandas as pd

print("请提前检查奖励积分配置！！！！！")
print("请提前检查奖励积分配置！！！！！")
print("请提前检查奖励积分配置！！！！！")

server = input("server:")
activityId = int(input("activityid:"))
account = input("accoutid:")
level = int(input("level:"))

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
    server = "http://dact.gameyici.com"#构造修改玩家数据的函数
def RankIns(data,host="https://dqa.hphorse.net"):
    url_banding = "{host}/BI/open/disMatch".format(host=host)
    headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "Content-Type": "application/json",
    "Origin": "{host}".format(host=host),
    "Referer": "{host}/BI/open/disMatch".format(host=host)
    }

    res3 = requests.post(url_banding, data, headers=headers)
    res = res3.text
    # res = json.loads(res)
    # res = res["msg"]
    print(res)
# data = {}




#创建奖品名称映射
mine = {}
total = {}#

item = {}
table_item = pd.read_excel("E:\\FA\\nfa-config\\excel\\DataFile\\ItemTemplate.xlsx")
table_item_val = table_item.values
for i in range(3,len(table_item_val)):
    item[str(table_item_val[i][0])] = table_item_val[i][1]


#打开配置文件
sr = open("E:\\PyTools\\dragon\\tools\\ScoreReward.txt","r")
for line in sr:
    line = line.replace("\n","")
#llll是配置，格式[分数，[[奖励1,数量],[奖励2,数量]]]
    llll = line.split("\t")

#===========================
    log_res = login_gm(server)                      #登录GM平台
    info = get_playerid(account, log_res,server)  #获取playerId
    player = info["playerid"]
    session = info["sessionid"]
    # player = 'lc8b8r' 
    lis = get_itemlist(player,session,account,log_res,server)
    lis = lis['item']
    lis_dic = json.loads(lis)
    tacc = {}#

    for tp in lis_dic:
        if tp["num"] != 0:
            tacc[(str(tp["id"]))+"-"+tp["name"]] = tp["num"]#新的
            old_tacc = total.get(account)
            if old_tacc is not None:
                if tacc.get((str(tp["id"]))+"-"+tp["name"]) != old_tacc.get((str(tp["id"]))+"-"+tp["name"]):
                    if old_tacc.get((str(tp["id"]))+"-"+tp["name"]) is not None:
                        print('='*(32-len(tp["name"])*2-len((str(tp["id"])))),(str(tp["id"]))+"-"+tp["name"],":",tp["num"],"-"*(10-len(str(tp["num"]))),"change:",tacc[(str(tp["id"]))+"-"+tp["name"]]-old_tacc.get((str(tp["id"]))+"-"+tp["name"]))
                    else:
                        print('='*(32-len(tp["name"])*2-len((str(tp["id"])))),(str(tp["id"]))+"-"+tp["name"],":",tp["num"],"-"*(10-len(str(tp["num"]))),"change:",tacc[(str(tp["id"]))+"-"+tp["name"]])
    total[account] = tacc
    


    print("\n\n")
    print("==========================\n")
#修改玩家积分
    data_rank = []
    data_faker = '{"pid":"","level":0,"activityId":0,"score":0}'
    data_faker = json.loads(data_faker)
    data_faker["pid"] = player
    data_faker["level"] = level
    data_faker["activityId"] = activityId
    data_faker["score"] = int(llll[0])-1
    data_faker = json.dumps(data_faker)
    data_rank.append(data_faker)
    RankIns(str(data_rank),server)

    print("==========================\n"+account,":")




#统计奖励数量并打印
    for reward in eval(llll[1]):
        if reward[0] in mine:
            mine[reward[0]] += reward[1]
        else:
            mine[reward[0]] = reward[1]
        print("{name}:{num}".format(name=item[str(reward[0])],num=reward[1]))#mine[reward[0]]))
    # for i in mine:
    #     print("{name}:{num}".format(name=item[str(i)],num=mine[i]))
    running = input("contune?")
    while running == '1':
        #===========================
        log_res = login_gm(server)                      #登录GM平台
        info = get_playerid(account, log_res,server)  #获取playerId
        player = info["playerid"]
        session = info["sessionid"]
        # player = 'lc8b8r' 
        lis = get_itemlist(player,session,account,log_res,server)
        lis = lis['item']
        lis_dic = json.loads(lis)
        tacc = {}#

        for tp in lis_dic:
            if tp["num"] != 0:
                tacc[tp["name"]] = tp["num"]#新的
                old_tacc = total.get(account)
                if old_tacc is not None:
                    if tacc.get(tp["name"]) != old_tacc.get(tp["name"]):
                        if old_tacc.get(tp["name"]) is not None:
                            print('='*(25-len(tp["name"])*2),tp["name"],":",tp["num"],"-"*(10-len(str(tp["num"]))),"change:",tacc[tp["name"]]-old_tacc.get(tp["name"]))
                        else:
                            print('='*(25-len(tp["name"])*2),tp["name"],":",tp["num"],"-"*(10-len(str(tp["num"]))),"change:",tacc[tp["name"]])
        total[account] = tacc
        


        print("\n\n")
        print("==========================\n")
        running = input("contune?")

sr.close()
input("continue")








