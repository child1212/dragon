#%%
import time
import requests
import json
import copy
import os
pack_pos = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
import sys
sys.path.append('{pack_pos}\\function'.format(pack_pos=pack_pos))
from func_dragon import *
from xieyi import *
from player_data import *
param_ad = {}

#################################################
server = "qa"
# accounts = {"ol3699","ol3698"}
# accounts = {"ol3495","ol3497"}
# accounts = {"ol3499","ol3498"}
accounts = {"ol4599","ol4598"}



# 锁分组
param_ad["locked"] = 1
# 分组
param_ad["group"] = 6
# 礼包
# param_ad["recordInfos"] = []




if server == "ntest":
    server = "http://192.168.1.143"
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

    palyerdata = player_data(playerinfo)
    ad = Ads(palyerdata)
    #复制数据
    p = copy.deepcopy(ad.data)
    for key in param_ad:
        p[key] = param_ad[key]
    change_Param(ad,log_res,server,p)
    print(p)


# %%
# 单发道具
item_id = "2100"
num = -50
for account in accounts:
    info = get_playerid(account, log_res,server)    #��ȡplayerId
    player = info['playerid']
    session = info['sessionid']

    send_gift(item_id,num,player,session,account,log_res,server)
