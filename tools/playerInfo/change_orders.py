#%%
import time
import requests
import json
import copy
import os
import item_xlsx

pack_pos = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
import sys
sys.path.append('{pack_pos}\\function'.format(pack_pos=pack_pos))
from func_dragon import *
from xieyi import *
from player_data import *
param = {}

#################################################
server = "nqa"
accounts = {"mm0697"}

# # 锁分组
# param["locked"] = 1
# # 分组
# param["group"] = 4
item_dic = item_xlsx.item_table().result



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
    prop = OrderTask(palyerdata)
    #复制数据
    p = copy.deepcopy(prop.data)
    for key in param:
        p[key] = param[key]
    # change_Param(prop,log_res,server,p)
    # print(p)
    # for x in p.get("orderTask").get("orderTasks"):
    #     a = x.get("taskItems")
    #     e = 0
    #     for b in a:
    #         c = b.get("itemTemplateId")
    #         d = item_dic.get(int(c))
    #         e += d*b.get("count")
    #     print("position:",x.get("position"),":",e*1.48)

    
