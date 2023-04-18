#%%
import time
import requests
import json
import os
pack_pos = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
import sys
sys.path.append('{pack_pos}\\function'.format(pack_pos=pack_pos))
from func_dragon import *
from xieyi import *


server = "nqa"
accounts = {"yy0001","yy0000"}
player = ''



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

for account in accounts:
    player = ''
    print(account)
    log_res = login_gm(server)    
    if not player:
        res = get_playerid(account,log_res,server)           
        player = res["playerid"]
    playerinfo = get_player_info(account,player,server,log_res)

    info_dic =  {}

    for i in playerinfo["page"]["list"]:
        info_dic[i["key"]] = i["value"]

    properties = json.loads(info_dic["P{player}@{{{player}}}-Properties".format(player=player)])
    gifts = json.loads(info_dic["P{player}@{{{player}}}-gift".format(player=player)])
    recharge = json.loads(info_dic["P{player}@{{{player}}}-Recharge".format(player=player)])
    
    for line in recharge.get("subscribes"):
        r = json.loads(line)
        if r.get("subscribeInfos")[1] != []:
            expired= r.get("subscribeInfos")[1][0]["expired"]
            print("expired",expired)
            timeExpired = time.localtime(expired)
            expired_format = time.strftime("%Y-%m-%d %H:%M:%S",timeExpired)
            productId = r.get("subscribeInfos")[1][0]["productId"]
            print("商品:",productId,'--到期时间：',expired_format)
        else:
            print("没有订阅月卡！！！")
    if recharge.get("limitedTimeProduct") !=[]:
        rr = recharge.get("limitedTimeProduct")[0]
        rr =json.loads(rr)
        expiryTime = rr.get("expiryTime")
        expiryTime_format = time.localtime(expiryTime//1000)
        expiryTime_format = time.strftime("%Y-%m-%d %H:%M:%S",expiryTime_format)
        print("月卡到期时间:",expiryTime_format)

    if gifts["monthGifts"] != []:
        month = json.loads(gifts["monthGifts"][0])
        lastAwardTime = month.get("lastAwardTime")
        if lastAwardTime != 0:
            timeLastAwardTime = time.localtime(lastAwardTime//1000)
            lastAwardTime_format = time.strftime("%Y-%m-%d %H:%M:%S",timeLastAwardTime)
            print("上次领奖时间：",lastAwardTime_format)
        lastDayUpdated = month.get("lastDayUpdated")
        if lastDayUpdated != 0:
            timeLastDayUpdated = time.localtime(lastDayUpdated//1000)
            lastDayUpdated_format = time.strftime("%Y-%m-%d %H:%M:%S",timeLastDayUpdated)
            print("上次刷新时间：",lastDayUpdated_format)
        factoryFreeUsed = month.get("factoryFreeUsed")
        print("工厂次数剩余：",5-factoryFreeUsed)