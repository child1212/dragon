#%%
import sys
sys.path.append('D:\\pyprogram\\PyTestTools\\dragon\\function')
from func_dragon import *

server = "qa"                               #服务器前缀<dev:"tlogin", qa:"qausa">  #

if server == "38":
    server = "http://dtest.gameyici.com"
elif server == "qa":
    server = "https://dqa.hphorse.net"


log_res = login_gm(server)                      #登录GM平台

for i in range(1900, 1910):
    try:
        account = "{n}".format(n=str(i))
        info = get_playerid(account, log_res,server)    #获取playerId
        player = info['playerid']
        session = info['sessionid']
        result = untie(player,session,account,log_res,server)
        print('解绑账号  {acc}  :  {p}----------------------------{result}'.format(acc=account,p=player,result=result))
    except:
        print('解绑账号  {acc}  ----------------------------------没有该账号'.format(acc=account))
# %%
