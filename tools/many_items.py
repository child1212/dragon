
#%%
import sys
sys.path.append('D:\\pyprogram\\PyTestTools\\dragon\\function')
import time
from func_dragon import *


print("start time:",time.asctime(time.localtime()))
account = "Fgy0030"
num = 3000
server = "http://10.0.102.197"                               
# item = items()

table = open("D:\\pyprogram\\PyTestTools\\dragon\\tools\\ItemTemplate.csv",'r')
log_res = login_gm(server)                      #登录GM平台
info = get_playerid(account, log_res,server)    #获取playerId
player = info['playerid']
session = info['sessionid']

for line in table:
    line_l = line.split(",")
    if line_l[0] == '':
        break
    if "级" not in line_l[1] and "icon4" not in line_l[4] and "icon5" not in line_l[4]:
        result = send_gift(line_l[0], num, player,session, account, log_res,server)
        print(line_l[0],line_l[1], num,result)
table.close()
print("Mission Completed!")



#%%
def test(**kwargs):
    print(kwargs['a'])

test(a=1, b=2)
# %%
