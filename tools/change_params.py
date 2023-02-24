#%%
import time
import requests
import json
import sys
sys.path.append('D:\\pyprogram\\PyTestTools\\dragon\\function')
from func_dragon import *
from xieyi import *
param = {}

###############################################
server = "ntest"
account = 'xx0000'
player = ''
param["nickName"] = "毛阿毛"
param["level"] = 20

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


log_res = login_gm(server)    
if not player:
    res = get_playerid(account,log_res,server)           
    player = res["playerid"]
playerinfo = get_player_info(account,player,server,log_res)

info_dic =  {}

for i in playerinfo["page"]["list"]:
    info_dic[i["key"]] = i["value"]




change_Properties(info_dic,player,log_res,server,param)

