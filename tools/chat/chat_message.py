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

account = "tan111"
cid = "1_3hapgn"
message = "this is a test message!"
server = "38"
version = "31.1.0"



if server == "38":
    server = "http://dtest.gameyici.com"
elif server == "qa":
    server = "https://dqa.hphorse.net"

log = login(account,server,version)
res_1002 = entergame(log,server,version)

#解码1002数据
game_data =CoreModuleMsg_pb2.EnterGameResponse()
game_data.ParseFromString(res_1002.bodys[0].msgBody)
for i in range(1):
    message = "this is a test message!{time}".format(time=time.asctime(time.localtime()))
    chat_message(log,server,version,cid,message,game_data)
    time.sleep(5)
# %%
