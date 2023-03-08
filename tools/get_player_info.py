#%%
import time
import requests
import json
import os
pack_pos = os.path.dirname(os.path.dirname(__file__))
import sys
sys.path.append('{pack_pos}\\function'.format(pack_pos=pack_pos))
sys.path.append('{pack_pos}\\package'.format(pack_pos=pack_pos))

from func_dragon import *


server = "https://nfa-test.bettagames.com"
player = 'xx0000'
account = ''
host = server

log_res = login_gm(server)               
playerinfo = get_player_info(account,player,server,log_res)

info_dic =  {}

for i in playerinfo["page"]["list"]:
    # info_dic[i["key"]] = i["value"]
    k = i["key"].split("-")
    info_dic[k[-1]] = i["value"]

table_item = open("D:\\pyprogram\\PyTestTools\\dragon\\tools\\ItemTemplate-n.csv","r",encoding="utf-8-sig")

#创建奖品名称映射
item = {}
for line in table_item:
    line_l = line.split(",")
    item[str(line_l[0])] = line_l[1]
table_item.close()




