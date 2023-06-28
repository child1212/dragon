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
server = "38"
accounts = {"li2023"}
# 等级
# param["growthFund"] = '{"@class":"com.game.mongo.model.PlayerGrowthFund","shopId":null,"rewardIds":["java.util.ArrayList",[]],"shopIds":["java.util.ArrayList",[]]}'
# # 等级
# param["level"] = 30
# 昵称
# param["nickName"] = "gold"
# 时间差

# from_current_time = True
# d,h,m = 20,0,0
# param["timeOffset"] = (((d*24)+h)*60+m)*60*1000
# template_time = param["timeOffset"]


# 经验
# param["exp"] = 106799

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
    prop = GrowthFund(palyerdata)
    #复制数据
    p = copy.deepcopy(prop.data)

    for key in param:
        p[key] = param[key]


    # change_Param(prop,log_res,server,p)
    print(p)



# %%
