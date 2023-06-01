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
param = {}

###############################################
server = "ntest"
accounts = {"mm0698"}

# #等级
# param["level"] = 15
# # #昵称
# param["nickName"] = "gold"
# #时间差

# from_current_time = True
# d,h,m = 0,1,0
# param["timeOffset"] = (((d*24)+h)*60+m)*60*1000
# template_time = param["timeOffset"]

# #经验
# param["exp"] = 200

# #最后一次付费时间
# param["lastRechargeTime"] = (time.time()-60*24*3600)*1000

#支付金额
# param["totalPayAmount"] = 1000000      

# #皮肤 ["27351","27352","27350","27353"]
# param["heroineSkins"] = [27202]   

# #隐藏VIP等级开关
# param["hideVipLevel"] = True



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

    key = "P{playerid}@{{{playerid}}}-Properties".format(playerid=player)
    
    if param.get("timeOffset") and from_current_time == True:
        param["timeOffset"] = template_time+json.loads(info_dic[key])["timeOffset"]
        print(param["timeOffset"])

    change_Properties(info_dic,player,log_res,server,param)

    print(account,'finish')

# %%
