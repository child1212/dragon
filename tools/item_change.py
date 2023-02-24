#%%
import sys
sys.path.append('D:\\pyprogram\\PyTestTools\\dragon\\function')
import time
from func_dragon import *
import os


#######################################################################################
#道具各项参数d6e0c013d2c377bbeb3f56a262cf3b99
accounts = {"te0000","xx0000"}                               #账号                             #
server = "ntest"                                    #服务器前缀<dev:"tlogin", qa:"qausa">  #
#######################################################################################

if server == "ntest":
    server = "https://nfa-test.bettagames.com"
elif server == "nqa":
    server = "https://qa-nfa.hphorse.net"
elif server == "nrelease":
    server = "https://online-nfa.hphorse.net"
elif server == "38":
    server = "http://dtest.gameyici.com"
elif server == "qa":
    server = "https://dqa.hphorse.net"
elif server == "dragon":
    server = "https://dragon.hphorse.net"
elif server == "act":
    server = "http://dact.gameyici.com"

total = {}#
run = ''
while run == '':
    for account in accounts:
        print(account+":","\n=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=")


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
                tacc[(str(tp["id"]))+"-"+tp["name"]] = tp["num"]#新的
                old_tacc = total.get(account)
                if old_tacc is not None:
                    if tacc.get((str(tp["id"]))+"-"+tp["name"]) != old_tacc.get((str(tp["id"]))+"-"+tp["name"]):
                        if old_tacc.get((str(tp["id"]))+"-"+tp["name"]) is not None:
                            print('='*(32-len(tp["name"])*2-len((str(tp["id"])))),(str(tp["id"]))+"-"+tp["name"],":",tp["num"],"-"*(10-len(str(tp["num"]))),"change:",tacc[(str(tp["id"]))+"-"+tp["name"]]-old_tacc.get((str(tp["id"]))+"-"+tp["name"]))
                        else:
                            print('='*(32-len(tp["name"])*2-len((str(tp["id"])))),(str(tp["id"]))+"-"+tp["name"],":",tp["num"],"-"*(10-len(str(tp["num"]))),"change:",tacc[(str(tp["id"]))+"-"+tp["name"]])
                    else:
                        print('='*(32-len(tp["name"])*2-len((str(tp["id"])))),(str(tp["id"]))+"-"+tp["name"],":",tp["num"])
                else:
                    print('='*(32-len(tp["name"])*2-len((str(tp["id"])))),(str(tp["id"]))+"-"+tp["name"],":",tp["num"])
        total[account] = tacc
        


        # print("\n\n")
    print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=\n")
    run = input("contune?")









# %%
