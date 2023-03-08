#%%
import time
import requests
import json
import os
pack_pos = os.path.dirname(os.path.dirname(__file__))
import sys
sys.path.append('{pack_pos}\\function'.format(pack_pos=pack_pos))
sys.path.append('{pack_pos}\\package'.format(pack_pos=pack_pos))
import random
from func_dragon import *
from xieyi import *


param = {}

###############################################
server = "ntest"
account = 'xx0000'
player = ''
version = '3.1.0'
# param["level"] = 20

################################################

if server == "ntest":
    server = "https://nfa-test.bettagames.com"
elif server == "nqa":
    server = "https://qa-nfa.hphorse.net"
elif server == "38":
    server = "http://dtest.gameyici.com"
elif server == "qa":
    server = "https://dqa.hphorse.net"
elif server == "act":
    server = "http://dact.gameyici.com"

frames = ("24000","24001")
log_res = login_gm(server)    
for j in range(100):
    account = 'act{j}'.format(j=j)
    param["frame"] = random.choice(frames)
    param["hideVipLevel"] = False
    param["totalPayAmount"] = random.choice([100,1000,3000,6000,12000,32000,120000,220000,520000,1200000])
    param["lastRechargeTime"] = 1677049417000
    

    res = get_playerid(account,log_res,server)           
    player = res["playerid"]
    playerinfo = get_player_info(account,player,server,log_res)

    info_dic =  {}

    for i in playerinfo["page"]["list"]:
        info_dic[i["key"]] = i["value"]

    change_Properties(info_dic,player,log_res,server,param)

    log = login(account,server,version)
    entergame(log,server,version)
    get_vip(log,server,version)
    print(account)

# %%
