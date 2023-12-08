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



server = "ntest"
accounts = {"onl797"}
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


one = (61001,61002,61003,61004,61005,61006,61007,61009,61010,61011,61012,61017,61018,61019,61025)
two = (61008,61013,61014,61015,61020,61021,61022,61026,61027,61028,61033,61034,61041)
three =(61016,61023,61029,61030,61035,61036,61037,61042,61043,61049)
four = (61024,61031,61038,61039,61044,61045,61050,61051,61052)
five = (61032,61040,61046,61047,61048,61053,61054,61055,61056)
temp = {61007,61015,61029,61038,61056}
temp = {61027}
for itemid in range(61001,61057):
    if itemid in temp:
        continue
    item_id = str(itemid)
    num = 1
    for account in accounts:
        info = get_playerid(account, log_res,server)    #��ȡplayerId
        player = info['playerid']
        session = info['sessionid']

        send_gift(item_id,num, player,session, account, log_res,server)


#%%
#补充发放的道具基准
xxx = {61002:2,61013:2,61023:3,61031:3,61040:3,60015:1}
xxx = {61002:2,61013:1,61023:3,61031:3,61040:3,60012:1,1003:10000,1001:10000,10000001:5000}
for itemid in xxx.keys():
    item_id = str(itemid)
    num = xxx[itemid]
    for account in accounts:
        info = get_playerid(account, log_res,server)    #��ȡplayerId
        player = info['playerid']
        session = info['sessionid']

        send_gift(item_id,num, player,session, account, log_res,server)