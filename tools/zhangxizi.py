#%%
import sys
sys.path.append('D:\\pyprogram\\PyTestTools\\dragon\\function')
import time
from func_dragon import *
import os




def send_d(account):
    print("start time:",time.asctime(time.localtime()))
    account = str(account)
    level = "3"
    num = 1
    server =1 #'https://dragon.hphorse.net'


    players = set(["zw73jj","m09zru","tcsihl", "7ciitk", "t7q9h8"])



    # item = items()
    pat = os.getcwd()
    
    table = open("{pat}\\MagicalCreaturesTemplate.csv".format(pat=pat),'r',encoding="utf-8")
    log_res = login_gm(server)                      #��¼GMƽ̨
    info = get_playerid(account, log_res,server)    #��ȡplayerId
    player = info['playerid']
    session = info['sessionid']

    if player not in players:
        print(players)
        return
    players.remove(player)
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
    send_gift(27500, 1, player,session, account, log_res,server)
    table.close()
    print("playerid:-{player}\nMission Completed!".format(player=player))


    #----------------------------------------------------------------------------

    print("start time:",time.asctime(time.localtime()))
    num = 900
    # item = items()

    pat = os.getcwd()
    table = open("{pat}\\ItemTemplate.csv".format(pat=pat),'r',encoding='utf-8')

    for line in table:
        line_l = line.split(",")
        if line_l[0] == '':
            break
        if "级" not in line_l[1] and "4" not in line_l[6] and "-1" not in line_l[6] and "icon4" not in line_l[4] and "icon5" not in line_l[4]:
            if "3" not in line_l[6]:
                result = send_gift(line_l[0], num, player,session, account, log_res,server)
                print(line_l[0],line_l[1], num,result)
                


    send_gift(1001, 100000, player,session, account, log_res,server)
    send_gift(1003, 100000, player,session, account, log_res,server)
    table.close()
    print("playerid:-{player}\nMission Completed!".format(player=player))


accs = []
for account in accs:
    send_d(account)
# %%
