
#%%
import sys
sys.path.append('D:\\pyprogram\\PyTestTools\\dragon\\function')
import time
from func_dragon import *
import os

print("start time:",time.asctime(time.localtime()))
account = "fenjie"
server = "qa"                           
item_type = (24,27,36)
'''
24:头像框
27:皮肤,帽子
36:帽子图纸
'''
# item = items()



if server == "38":
    server = "http://dtest.gameyici.com"
elif server == "qa":
    server = "https://dqa.hphorse.net"
pat = os.path.dirname(__file__)
table = open("{pat}\\ItemTemplate.csv".format(pat=pat),'r',encoding='utf-8')
log_res = login_gm(server)                      #��¼GMƽ̨
info = get_playerid(account, log_res,server)    #��ȡplayerId
player = info['playerid']
session = info['sessionid']

for line in table:
    line_l = line.split(",")
    if line_l[0] == '':
        break
    
    if int(line_l[7]) in item_type:
        result = send_gift(line_l[0], 1, player,session, account, log_res,server)
        print(line_l[0],line_l[1], 1,result)
            


# send_gift(1001, 100000, player,session, account, log_res,server)
# send_gift(1003, -100000, player,session, account, log_res,server)
table.close()
print("playerid:-{player}\nMission Completed!".format(player=player))




# %%
