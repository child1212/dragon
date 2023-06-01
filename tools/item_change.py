#%%
import os
pack_pos = os.path.dirname(os.path.dirname(__file__))
import sys
sys.path.append('{pack_pos}\\function'.format(pack_pos=pack_pos))
import time
from func_dragon import *


#######################################################################################
#dragon : d6e0c013d2c377bbeb3f56a262cf3b99\603681214128417
#FA : 91a4a00cc23bdae216d5dc2519da2c77\623293505cf755ed47851789c0bb1c48
accounts = {"li2022"}                            #账号                                 #
server = "38"                                    #服务器前缀<dev:"tlogin", qa:"qausa">  #
printAll = False
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
no = 501
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
            tacc[(str(tp["id"]))+"-"+tp["name"]] = tp["num"]#新的
            old_tacc = total.get(account)
            # 有旧的
            if old_tacc is not None:
                #新旧不一
                if tacc.get((str(tp["id"]))+"-"+tp["name"]) != old_tacc.get((str(tp["id"]))+"-"+tp["name"]):
                    print('='*(32-len(tp["name"])*2-len((str(tp["id"])))),(str(tp["id"]))+"-"+tp["name"],":",tp["num"],"-"*(10-len(str(tp["num"]))),"change:",tacc[(str(tp["id"]))+"-"+tp["name"]]-old_tacc.get((str(tp["id"]))+"-"+tp["name"]))
                #新旧一样
                else:
                    if printAll and tp["num"] != 0:
                        print('='*(32-len(tp["name"])*2-len((str(tp["id"])))),(str(tp["id"]))+"-"+tp["name"],":",tp["num"])
                    else:
                        pass
            # 没有旧的
            else:
                if tp["num"] != 0:
                    print('='*(32-len(tp["name"])*2-len((str(tp["id"])))),(str(tp["id"]))+"-"+tp["name"],":",tp["num"])
        total[account] = tacc
        


        # print("\n\n")
    print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=\n")
    run = input("contune?")
    # os.system("adb shell input tap 2071 718")
    # os.system("adb shell input tap 1619 914")
    # os.system("adb exec-out screencap -p >e://screenshot/upgrade{no}.jpg".format(no=no))
    # os.system("adb shell input tap 1619 914")
    
    # os.system("python D:\\pyprogram\\PyTestTools\\dragon\\tools\\template\\globalProgress.py")
    no += 1








# %%

# %%

# %%
