#%%
total = {}#
#%%
import sys
sys.path.append('D:\\pyprogram\\PyTestTools\\dragon\\function')
import time
from func_dragon import *
import os


#######################################################################################
#道具各项参数
accounts = {"li0000","li0001"}                               #账号                             #
server = "https://nfa-test.bettagames.com"                               #服务器前缀<dev:"tlogin", qa:"qausa">  #
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
    tacc = {}#

    for tp in lis_dic:
        if tp["num"] != 0:
            tacc[tp["name"]] = tp["num"]#新的
            old_tacc = total.get(account)
            if old_tacc is not None:
                if tacc.get(tp["name"]) != old_tacc.get(tp["name"]):
                    if old_tacc.get(tp["name"]) is not None:
                        print(tp["name"],":",tp["num"],'='*(30-len(tp["name"])*2-len(str(tp["num"]))),"change:",tacc[tp["name"]]-old_tacc.get(tp["name"]))
                    else:
                        print(tp["name"],":",tp["num"],'='*(30-len(tp["name"])*2-len(str(tp["num"]))),"change:",tacc[tp["name"]])
                else:
                    print(tp["name"],":",tp["num"])
            else:
                print(tp["name"],":",tp["num"])
    total[account] = tacc
    


    print("\n\n")









# %%
