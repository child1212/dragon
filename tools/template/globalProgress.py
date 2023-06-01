#%%
import time
import pandas as pd
import json
import os
pack_pos = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
import sys
sys.path.append('{pack_pos}\\function'.format(pack_pos=pack_pos))
from func_dragon import *
from xieyi import *
param = {}
#定义修改函数
def change_globalProgress(info,playerid,login_res,host,params):
    key = "P{playerid}@{{{playerid}}}-globalProgress".format(playerid=playerid)
    value = info[key]
    value = json.loads(value)
    task = json.loads(value["task"])
    for i in params:
        task[i] = params[i]
    task = json.dumps(task)
    value["task"] = task
    value = json.dumps(value)    

    url_itemlist = "{host}/BI/bi/bieditplayerdata/update".format(host=host)
    data_itemlist = '{"rowKey":"","rowValue":"","note":null,"serverId":null}'
    data_itemlist = json.loads(data_itemlist)
    data_itemlist["rowKey"] = key
    data_itemlist["rowValue"] = value
    data_itemlist = json.dumps(data_itemlist)

    headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
    "Content-Type": "application/json",
    "Origin": "{host}".format(host=host),
    "Referer": "{host}/BI/modules/bi/biqatool.html".format(host=host),
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    }

    res_item = requests.post(url_itemlist, data=data_itemlist,cookies = login_res.cookies, headers=headers)
    res_list = res_item.text
    res_list = json.loads(res_list)
    return res_list

###############################################
server = "qa"
accounts = {"3298"}
player = ''

tasks = [[2002,25],[2003,25],[2004,25],[2001,40]]
rewards = [[20000,1,1200,200,70],[15000,3,1200,200,10],[20000,1,1200,200,20],[2100,1,1201,350,60],[20000,1,1201,350,20],[42000,3,1201,350,20],[20000,1,1201,350,20],[27530,1,1201,500,80]]
prices = {1200:1.99,1201:2.99}
################################################

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

#创建奖品名称映射
project = "DFA"
if project == "NFA":
    table_item = pd.read_excel("E:\\town\\FA\\nfa-config\\excel\\DataFile\\ItemTemplate.xlsx")
    table_item = table_item.values
elif project == "DFA":
    table_item = pd.read_excel("E:\\town\\dragon\\dragon-config\\excel\\DataFile\\ItemTemplate.xlsx")
    table_item = table_item.values
item = {}
for line in table_item:
    item[line[0]] = line[1]



for account in accounts:
    player = ''
    log_res = login_gm(server)    
    if not player:
        res = get_playerid(account,log_res,server)           
        player = res["playerid"]
    playerinfo = get_player_info(account,player,server,log_res)

    info_dic =  {}

    for i in playerinfo["page"]["list"]:
        info_dic[i["key"]] = i["value"]



    data = json.loads(info_dic["P{player}@{{{player}}}-globalProgress".format(player=player)])
    # print(data)
    task = json.loads(data["task"])
    history = data["history"]
    print("已领取：",task["awarded"])
    end = time.asctime(time.localtime(task["end"]//1000))
    print("结束时间：",end)
    print("任务索引：",task["turn"])
    print("任务内容：",item[tasks[task["taskIndex"]][0]],tasks[task["taskIndex"]][1])
    print("任务进度：",task["finishNum"])
    print("轮次",task["num"])
    print("任务普通奖励：",item[rewards[task["turn"]-1][0]],rewards[task["turn"]-1][1])
    if task.get("specialEntry"):
        print("幸运礼包：",item[int(task["specialEntry"]["itemId"])],task["specialEntry"]["count"])
        print("礼包价格：",prices[rewards[task["turn"]-1][2]])
    if history != []:
        print("======================")
        print("待领取：")
        for line in history:
            pa = json.loads(line)
            if not pa.get("awarded"):
                print("任务普通奖励：",item[rewards[pa["turn"]-1][0]],rewards[pa["turn"]-1][1])
            if pa.get("specialEntry"):
                print("幸运礼包：",item[int(pa["specialEntry"]["itemId"])],pa["specialEntry"]["count"])
                print("礼包价格：",prices[rewards[pa["turn"]-1][2]])
            print("")


    #完成任务
    # params = {}
    # params["finishNum"] = 40
    # change_globalProgress(info_dic,player,log_res,server,params)
    #完成任务


