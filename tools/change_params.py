#%%
import time
import requests
import json
import os
pack_pos = os.path.dirname(os.path.dirname(__file__))
import sys
sys.path.append('{pack_pos}\\function'.format(pack_pos=pack_pos))
from func_dragon import *
from xieyi import *
param = {}

###############################################
server = "qa"
account = 'li2005'
player = ''

# #等级
# param["level"] = 14
# #昵称
param["nickName"] = "回归"      
# #时间差
d,h,m = 33,0,0
param["timeOffset"] = (((d*24)+h)*60+m)*60*1000   
# #经验
# param["exp"] = 22299             
# #最后一次付费时间
# param["lastRechargeTime"] = time.time()*1000    
# #支付金额
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


log_res = login_gm(server)    
if not player:
    res = get_playerid(account,log_res,server)           
    player = res["playerid"]
playerinfo = get_player_info(account,player,server,log_res)

info_dic =  {}

for i in playerinfo["page"]["list"]:
    info_dic[i["key"]] = i["value"]




change_Properties(info_dic,player,log_res,server,param)

