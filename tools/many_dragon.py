#%%
import sys
sys.path.append('D:\\pyprogram\\PyTestTools\\dragon\\function')
import time
from func_dragon import *
import os

print("start time:",time.asctime(time.localtime()))
account = "嘻嘻嘻5"
level = ""
server = "http://dtest.gameyici.com"                           
# item = items()
pat = os.getcwd()
table = open("{pat}\\MagicalCreaturesTemplate.csv".format(pat=pat),'r')
log_res = login_gm(server)                      #��¼GMƽ̨
info = get_playerid(account, log_res,server)    #��ȡplayerId
player = info['playerid']
session = info['sessionid']

for line in table:
    line_l = line.split(",")
    if line_l[0] == '':
        break
    if "{level}".format(level=level) in line_l[3]:
        result = send_gift(line_l[0], 1, player,session, account, log_res,server)
        print(line_l[0],line_l[3], 1,result)
send_gift(1001, 10000, player,session, account, log_res,server)
# send_gift(1003, 100000, player,session, account, log_res,server)
table.close()
print("playerid:-{player}\nMission Completed!".format(player=player))


# %%