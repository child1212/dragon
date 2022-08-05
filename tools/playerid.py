# %%
import sys
sys.path.append('D:\\pyprogram\\PyTestTools\\dragon\\function')
from xieyi import *

account = "1960"
server = "38" 
version = "19.1.0"


if server == "38":
    server = "http://dtest.gameyici.com"
elif server == "qa":
    server = "https://dqa.hphorse.net"
elif server == "dragon":
    server = "https://dragon.hphorse.net"


for i in range(100,200):
    account = "qinqi{i}".format(i=i)
    log = login(account,server,version)
    print(account,":", log.playerId)
# %%
