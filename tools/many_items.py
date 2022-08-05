
#%%
import sys
sys.path.append('D:\\pyprogram\\PyTestTools\\dragon\\function')
import time
from func_dragon import *
import os

print("start time:",time.asctime(time.localtime()))
account = "1909"
num = 2000
server = "qa"                           
# item = items()



if server == "38":
    server = "http://dtest.gameyici.com"
elif server == "qa":
    server = "https://dqa.hphorse.net"
pat = os.getcwd()
table = open("{pat}\\ItemTemplate.csv".format(pat=pat),'r',encoding='utf-8')
log_res = login_gm(server)                      #��¼GMƽ̨
info = get_playerid(account, log_res,server)    #��ȡplayerId
player = info['playerid']
session = info['sessionid']
item_type = (2,3,5,7,13,15,16,18,25,32)

# for item in range(2020,2032):
#     send_gift(item, 10, player,session, account, log_res,server)

for line in table:
    line_l = line.split(",")
    if line_l[0] == '':
        break
    
    if "龙" not in line_l[1] and"icon4" not in line_l[4] and "icon5" not in line_l[4]:
        if int(line_l[7]) in item_type:
    # if "基因" in line_l[1] and "显示" not in line_l[1]:
            result = send_gift(line_l[0], num, player,session, account, log_res,server)
            print(line_l[0],line_l[1], num,result)
                


send_gift(1001, 100000, player,session, account, log_res,server)
send_gift(1003, 100000, player,session, account, log_res,server)
table.close()
print("playerid:-{player}\nMission Completed!".format(player=player))




# %%
