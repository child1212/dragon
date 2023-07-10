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
param_mc = {}

#################################################
server = "38"
accounts = {"ol3497","ol3496"}
accounts = {"ol3489","ol3488"}

# 锁分组
# param_mc["skins"] = {}
# 分组
# param_mc["group"] = 3





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
    print(account)
    player = ''
    log_res = login_gm(server)    
    if not player:
        res = get_playerid(account,log_res,server)           
        player = res["playerid"]
    playerinfo = get_player_info(account,player,server,log_res)

    palyerdata = player_data(playerinfo)
    mc = MagicalCreature(palyerdata)
    #复制数据
    p = copy.deepcopy(mc.data)
    for key in param_mc:
        p[key] = param_mc[key]
    change_Param(mc,log_res,server,p)
    # print(p)
    print(mc.data.get("skins"))
    


