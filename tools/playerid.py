# %%
import sys
sys.path.append('D:\\pyprogram\\PyTestTools\\dragon\\function')
from xieyi import *

account = "1960"
server = "https://dqa.hphorse.net" 
version = "19.1.0"
for i in range(100,200):
    account = "new{i}".format(i=i)
    log = login(account,server,version)
    print(account,":", log.playerId)
# %%
