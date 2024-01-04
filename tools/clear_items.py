#%%
import os
pack_pos = os.path.dirname(os.path.dirname(__file__))
import sys
sys.path.append('{pack_pos}\\function'.format(pack_pos=pack_pos))
import time
from func_dragon import *
import os




#在这里填写参数=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*
print("start time:",time.asctime(time.localtime()))
accounts = {"ol3498"}
server = 'qa'
#在这里填写参数=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*




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


for account in accounts:
    log_res = login_gm(server)                      #��¼GMƽ̨
    info = get_playerid(account, log_res,server)    #��ȡplayerId
    player = info['playerid']
    session = info['sessionid']
    clear_item(player,log_res,server)
    # send_gift(22000, 100, player,session, account, log_res,server)
    # send_gift(30000, 100, player,session, account, log_res,server)
    # send_gift(1002, 100000000, player,session, account, log_res,server)
    send_gift(1001, 100000, player,session, account, log_res,server)
    # send_gift(81003, 1000, player,session, account, log_res,server)
    # send_gift(83001, 1000, player,session, account, log_res,server)
    send_gift(1003, 100, player,session, account, log_res,server)
    # send_gift(14074, 1, player,session, account, log_res,server)





    print("playerid:-{player}\nItem cleared!".format(player=player))





# %%
# 批量清除道具
import sys
sys.path.append('D:\\pyprogram\\PyTestTools\\dragon\\function')
import time
from func_dragon import *
import os
print("start time:",time.asctime(time.localtime()))
server = 'act'

for account in range(2000,2007):

    if server == "38":
        server = "http://dtest.gameyici.com"
    elif server == "qa":
        server = "https://dqa.hphorse.net"
    elif server == "act":
        server = "http://dact.gameyici.com"

    log_res = login_gm(server)                      #��¼GMƽ̨
    info = get_playerid("li{account}".format(account=account), log_res,server)    #��ȡplayerId
    player = info['playerid']
    session = info['sessionid']
    clear_item(player,log_res,server)
    # send_gift(22000, 100, player,session, account, log_res,server)
    # send_gift(7005, 30, player,session, account, log_res,server)
    send_gift(1001, 0, player,session, account, log_res,server)
    send_gift(1003, 100000, player,session, account, log_res,server)


    print("playerid:-{player}\nItem cleared!".format(player=player))

# %%
