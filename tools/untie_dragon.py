#%%
import sys
sys.path.append('D:\\pyprogram\\PyTestTools\\dragon\\function')
from func_dragon import *

server = "http://dtest.gameyici.com"                               #服务器前缀<dev:"tlogin", qa:"qausa">  #

log_res = login_gm(server)                      #登录GM平台

for i in range(790, 800):
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
