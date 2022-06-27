#%%
import sys
sys.path.append('D:\\pyprogram\\PyTestTools\\dragon\\package')
sys.path.append('D:\\pyprogram\\PyTestTools\\dragon\\function')
from func_dragon import *
from xieyi import *
import GatewayModuleMsg_pb2
import CoreModuleMsg_pb2
import GMModuleMsg_pb2
import time
import requests

account = "rank101"
cid = "7b90mm"
server = "38"
version = "19.1.0"



if server == "38":
    server = "http://dtest.gameyici.com"
elif server == "qa":
    server = "https://dqa.hphorse.net"

for i in range(1,14):
    account = "teamteam{i}".format(i=i)
    log = login(account,server,version)
    res_1002 = entergame(log,server,version)

    #解码1002数据
    game_data =CoreModuleMsg_pb2.EnterGameResponse()
    game_data.ParseFromString(res_1002.bodys[0].msgBody)

    join_team(log,server,version,cid)
    # leave_team(log,server,version,cid)
# %%
