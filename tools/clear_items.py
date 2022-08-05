#%%
import sys
sys.path.append('D:\\pyprogram\\PyTestTools\\dragon\\function')
import time
from func_dragon import *
import os





print("start time:",time.asctime(time.localtime()))
account = "2199"
server = '38'





if server == "38":
    server = "http://dtest.gameyici.com"   
elif server == "qa":
    server = "https://dqa.hphorse.net"
log_res = login_gm(server)                      #��¼GMƽ̨
info = get_playerid(account, log_res,server)    #��ȡplayerId
player = info['playerid']
session = info['sessionid']

clear_item(player,log_res,server)
print("playerid:-{player}\nItem cleared!".format(player=player))


