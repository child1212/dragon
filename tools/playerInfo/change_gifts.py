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
param_gif = {}

#################################################
server = "nqa"
# accounts = {"899","onl899"}
# accounts = {"ol3698","ol3699"}
# accounts = {"ol3479","ol3478"}
accounts = {"onl796","onl797"}

# 礼包
param_gif["gifts"] = []





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

    palyerdata = player_data(playerinfo)
    gifts = gift(palyerdata)
    #复制数据
    p = copy.deepcopy(gifts.data)
    for key in param_gif:
        p[key] = param_gif[key]
    change_Param(gifts,log_res,server,p)
    print(p)


# %%
# 单发道具
item_id = "2100"
num = -330
for account in accounts:
    info = get_playerid(account, log_res,server)    #��ȡplayerId
    player = info['playerid']
    session = info['sessionid']

    send_gift(item_id,num,player,session,account,log_res,server)
