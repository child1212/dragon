# %%
import sys
sys.path.append('D:\\pyprogram\\PyTestTools\\dragon\\function')
from xieyi import *

account = "700"
server = "https://dqa.gameyici.com" 
version = "7.1.0"
log = login(account,server,version)
print("playerid:", log.playerId)
# %%
