
#%%
import sys
sys.path.append('D:\\pyprogram\\PyTestTools\\dragon\\function')
import time
from func_dragon import *
import os

print("start time:",time.asctime(time.localtime()))
account = "A2A90680-DAF1-4C12-8DAE-F814635F1839"
num = 500
server = "https://dqa.gameyici.com"                           
# item = items()
pat = os.getcwd()
table = open("{pat}\\ItemTemplate.csv".format(pat=pat),'r')
log_res = login_gm(server)                      #��¼GMƽ̨
info = get_playerid(account, log_res,server)    #��ȡplayerId
player = info['playerid']
session = info['sessionid']

for line in table:
    line_l = line.split(",")
    if line_l[0] == '':
        break
    if "级" not in line_l[1] and "4" not in line_l[6] and "-1" not in line_l[6] and "icon4" not in line_l[4] and "icon5" not in line_l[4]:
        if "3" not in line_l[6]:
            result = send_gift(line_l[0], num, player,session, account, log_res,server)
            print(line_l[0],line_l[1], num,result)
            


send_gift(1001, 100000, player,session, account, log_res,server)
send_gift(1003, 100000, player,session, account, log_res,server)
table.close()
print("playerid:-{player}\nMission Completed!".format(player=player))




# %%
