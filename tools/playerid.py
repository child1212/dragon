# %%
import os
pack_pos = os.path.dirname(os.path.dirname(__file__))
import sys
sys.path.append('{pack_pos}\\function'.format(pack_pos=pack_pos))
sys.path.append('{pack_pos}\\package'.format(pack_pos=pack_pos))
from xieyi import *

account = ""
server = "38" 
version = "22.1.0"


if server == "38":
    server = "http://dtest.gameyici.com"
elif server == "qa":
    server = "https://dqa.hphorse.net"
elif server == "dragon":
    server = "https://dragon.hphorse.net"


for i in range(2220,2300):
    account = "{i}".format(i=i)
    log = login(account,server,version)
    print(account,":", log.playerId)
# %%
