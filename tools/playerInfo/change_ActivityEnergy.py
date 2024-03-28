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
param = {}

#################################################
server = "ntest"
accounts = {"onl799"}



#energy
score = 500
actid = 13024
coefficient = 10
param["energy"] = score*coefficient-1



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
    prop = ActivityEnergy(palyerdata)
    #复制数据
    p = copy.deepcopy(prop.data)
    index_act = 0
    for i in range(len(p["acts"])):
        temp = json.loads(p["acts"][i])
        if temp['actId'] == str(actid):
            index_act = i
            break
    
    for key in param:
        dat = json.loads(p["acts"][index_act])
        dat[key] = param[key]
        p["acts"][index_act] = json.dumps(dat)
    
    # 改数据
    change_Param(prop,log_res,server,p)
    a = json.loads(p["acts"][index_act])




    print("-------",account)
    print("score:",a["energy"])
    print("group:",a["group"])



    

# %%
