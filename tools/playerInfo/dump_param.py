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
accounts = {"xin001"}
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
    log_res = login_gm(server)    
    if not player:
        res = get_playerid(account,log_res,server)           
        player = res["playerid"]
    playerinfo = get_player_info(account,player,server,log_res)

    info_dic =  {}

    for i in playerinfo["page"]["list"]:
        info_dic[i["key"]] = i["value"]

    properties = json.loads(info_dic["P{player}@{{{player}}}-Properties".format(player=player)])
    # t = properties.get("lastRechargeTime")
    # t = time.localtime(t//1000)
    # t = time.strftime("%Y-%m-%d / %H:%M:%S",t)
    # print(t)
    # for line in properties:

    #     print(line,properties[line])
    print("level:",properties.get("level"))
    print("exp  :",properties.get("exp"))
    