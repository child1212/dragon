#%%
import os
pack_pos = os.path.dirname(os.path.dirname(__file__))
import sys
sys.path.append('{pack_pos}\\function'.format(pack_pos=pack_pos))
sys.path.append('{pack_pos}\\package'.format(pack_pos=pack_pos))
from func_dragon import *
from xieyi import *

rrr = CoreModuleMsg_pb2.EnterGameResponse()
account = "9F4E719B-4BF9-44B4-B980-83540935FE65"
server = "https://dragon.hphorse.net"
version = "15.1.0"
log = login(account,server,version)
res = entergame(log,server,version)
rrr.ParseFromString(res.bodys[0].msgBody)
print(rrr)
# %%
