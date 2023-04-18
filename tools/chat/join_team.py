#%%
import os
pack_pos = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
import sys
sys.path.append('{pack_pos}\\function'.format(pack_pos=pack_pos))
sys.path.append('{pack_pos}\\package'.format(pack_pos=pack_pos))
from func_dragon import *
from xieyi import *
import GatewayModuleMsg_pb2
import CoreModuleMsg_pb2
import GMModuleMsg_pb2
import time
import requests

account = "rank101"
cid = "bke2s9"
server = "act"
version = "31.1.0"



if server == "38":
    server = "http://dtest.gameyici.com"
elif server == "qa":
    server = "https://dqa.hphorse.net"
elif server == "act":
    server = "http://dact.gameyici.com"


for i in range(30,60):
    account = "youhua00{i}".format(i=i)
    log = login(account,server,version)
    res_1002 = entergame(log,server,version)

    #解码1002数据
    game_data =CoreModuleMsg_pb2.EnterGameResponse()
    game_data.ParseFromString(res_1002.bodys[0].msgBody)

    join_team(log,server,version,cid)
    # leave_team(log,server,version,cid)
# %%
