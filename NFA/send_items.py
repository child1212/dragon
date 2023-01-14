
#%%
import sys
sys.path.append('D:\\pyprogram\\PyTestTools\\dragon\\function')
import time
from func_dragon import *
import os

print("start time:",time.asctime(time.localtime()))
account = "1008"
num = -20
server = "test"      
# items = (101001,102001,103001,104001,201001,202001)
items = (32002,1001)


if server == "test":
    server = "https://nfa-test.bettagames.com"

log_res = login_gm(server)                      #��¼GMƽ̨
info = get_playerid(account, log_res,server)    #��ȡplayerId
player = info['playerid']
session = info['sessionid']




for item in items:
    send_gift(item, num, player,session, account, log_res,server)

                


# send_gift(1001, 100000, player,session, account, log_res,server)
# send_gift(1003, 100, player,session, account, log_res,server)
print("playerid:-{player}\nMission Completed!".format(player=player))




# %%
