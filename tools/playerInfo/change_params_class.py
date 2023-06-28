#%%
import time
import requests
import json
import os
import copy
pack_pos = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
import sys
sys.path.append('{pack_pos}\\function'.format(pack_pos=pack_pos))
from func_dragon import *
from xieyi import *
from player_data import *
param = {}

#################################################
server = "ntest"
accounts = {"fa0700"}
# 等级
# param["level"] = 30
# 经验
# param["exp"] = 3399
# 昵称
# param["nickName"] = "gold"
# 时间差

from_current_time = True
d,h,m = 3,0,0
param["timeOffset"] = (((d*24)+h)*60+m)*60*1000
template_time = param["timeOffset"]



# 最后一次付费时间
# param["lastRechargeTime"] = (time.time()-60*24*3600)*1000

# 支付金额
# param["totalPayAmount"] = 1000000      

# 皮肤 ["27351","27352","27350","27353"]
# param["heroineSkins"] = [27202]   

# 隐藏VIP等级开关
# param["hideVipLevel"] = True


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
    prop = Properties(palyerdata)

    if param.get("timeOffset") and from_current_time == True:
        param["timeOffset"] = template_time+prop.data["timeOffset"]
        print(param["timeOffset"])

    for k in param:
        prop.data[k] = param[k]
    change_Param(prop,log_res,server,prop.data)


    

# %%
# 单发道具
item_id = "34000"
num = -97
for account in accounts:
    info = get_playerid(account, log_res,server)    #��ȡplayerId
    player = info['playerid']
    session = info['sessionid']

    send_gift(item_id,num, player,session, account, log_res,server)
