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
server = "nqa"
# accounts = {"370001","3700"}
# accounts = {"onl796","onl797"}
# accounts = {"ol3698","ol3699"}
# accounts = {"ol4598","ol4599"}
accounts = {"ol2098","ol2099"}
# accounts = {"ol4599","ol4598"}
accounts = {"onl799","onl798"}

# # 等级
# param["level"] = 14

# 经验
# param["exp"] = 1900

# 昵称
# param["nickName"] = "gold"

# 新渠道
# param["campaign"] = "23856992579970254"#"23851245022520315","17335329307"

# # 时间差
from_current_time = True
x = 1
if x == 1:
    d,h,m = 3,6,48
elif x == 2:
    d,h,m = 0,0,-5
elif x == 3:
    d,h,m = 0,0,52
elif x == 4:
    d,h,m = 0,0,0
param["timeOffset"] = (((d*24)+h)*60+m)*60*1000
template_time = param["timeOffset"]




# 最后一次付费时间
# param["lastRechargeTime"] = (time.time()-60*24*3600)*1000

# 支付金额
# param["totalPayAmount"] = 3333

# 皮肤 ["27351","27352","27350","27353"]
# param["heroineSkins"] = [27202]   

# 隐藏VIP等级开关
# param["hideVipLevel"] = True


if server == "ntest":
    server = "http://192.168.1.143"
elif server == "nqa":
    server = "https://qa-nfa.hphorse.net"
elif server == "nrelease":
    server = "https://online-nfa.hphorse.net"
elif server == "38":
    server = "http://192.168.1.140"
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

    # x = prop.data["exp"]
    # print(x-y)
    # y = x

    

# %%
# 单发道具
item_id = "1003"
num = 100000
for account in accounts:
    info = get_playerid(account, log_res,server)    #��ȡplayerId
    player = info['playerid']
    session = info['sessionid']

    send_gift(item_id,num, player,session, account, log_res,server)

# %%
