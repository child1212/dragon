#%%
import sys
sys.path.append('D:\\pyprogram\\PyTestTools\\dragon\\function')
import time
from func_dragon import *
import os





print("start time:",time.asctime(time.localtime()))
account = "1102"
level = "1"
num = 1
server = '38'







# item = items()
pat = os.getcwd()
if server == "38":
    server = "http://dtest.gameyici.com"   
elif server == "qa":
    server = "https://dqa.hphorse.net"
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
        result = send_gift(line_l[0], num, player,session, account, log_res,server)
        print(line_l[0],line_l[3], num,result)
send_gift(1001, 10000, player,session, account, log_res,server)
send_gift(2100, 1000, player,session, account, log_res,server)
send_gift(2008, 1000, player,session, account, log_res,server)
send_gift(7005, 1000, player,session, account, log_res,server)
table.close()
print("playerid:-{player}\nMission Completed!".format(player=player))


# %%

