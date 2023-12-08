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
accounts = {"max013"}



#energy
# param['levelId'] = '166'#已通关
# param['todayCnt'] = 15#今日已使用次数
# param['autoFinishState'] = 1
param['hangUpLevel'] = 34#挂机等级
# param['rewardIds'] = ['java.util.ArrayList', []]
# param['refreshTime'] = 1700104393935#次数刷新时间
# param['hangUpStart'] = 1700097734000#挂机开始时间
# param['autoFinishMaxLevelId'] = '40'
# param['inGame'] = False



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
    prop = Pve(palyerdata)
    #复制数据
    p = copy.deepcopy(prop.data)
    index_act = 0
    # for i in range(len(p["pve"])):
    temp = json.loads(p["pve"])

    
    for key in param:
        temp[key] = param[key]
        p["pve"] = json.dumps(temp)

    
    # 改数据
    change_Param(prop,log_res,server,p)
    print(temp)








    

# %%
