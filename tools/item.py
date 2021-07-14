#%%
import sys
sys.path.append('D:\\pyprogram\\PyTestTools\\dragon\\function')
import time
from func_dragon import *


print("start time:",time.asctime(time.localtime()))
account = "1010"
server = "https://dtest.gameyici.com"                               
# item = items()
item = [1001, 1002, 1003]              #钻石、金币、体力
num = [10000]                               #道具数量                           
while len(num) < len(item):
    num.append(1)


# senditems(account, item, num, server)
log_res = login_gm(server)                      #登录GM平台
info = get_playerid(account, log_res,server)    #获取playerId
player = info['playerid']
session = info['sessionid']
for i in range(len(item)):
    result = send_gift(item[i], num[i], player,session, account, log_res,server)
    print(item[i],num[i],result)

# %%
