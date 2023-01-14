#%%
import sys
sys.path.append('D:\\pyprogram\\PyTestTools\\dragon\\function')
import time
from func_dragon import *
import os


#######################################################################################
#道具各项参数
accounts = ("1896","1895")                               #账号                             #
server = "https://dqa.hphorse.net"                               #服务器前缀<dev:"tlogin", qa:"qausa">  #
#######################################################################################

for account in accounts:
    print("==========================\n"+account,":")


    log_res = login_gm(server)                      #登录GM平台
    info = get_playerid(account, log_res,server)  #获取playerId
    player = info["playerid"]
    session = info["sessionid"]
    # player = 'lc8b8r' 
    lis = get_itemlist(player,session,account,log_res,server)
    lis = lis['item']

    lis_dic = json.loads(lis)
    total = {}#
    tacc = {}#

    for tp in lis_dic:
        if tp["num"] != 0:
            tacc[tp["name"]] = tp["num"]#
            print(tp["name"],":",tp["num"])
    


    print("\n\n")









# %%
