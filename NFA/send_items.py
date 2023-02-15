
#%%
import sys
sys.path.append('D:\\pyprogram\\PyTestTools\\dragon\\function')
import time
from func_dragon import *
import os

print("start time:",time.asctime(time.localtime()))
account = "li0000"
num = 10000
server = "ntest"      
# items = (101001,102001,103001,104001,201001,202001)
# items = {2020,2021,2022,2023,31001,31002,31003,31004,32001,32002,1001}
items = {1001}

if server == "ntest":
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
