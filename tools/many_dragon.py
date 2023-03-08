#%%
import os
pack_pos = os.path.dirname(os.path.dirname(__file__))
import sys
sys.path.append('{pack_pos}\\function'.format(pack_pos=pack_pos))
sys.path.append('{pack_pos}\\package'.format(pack_pos=pack_pos))
import time
from func_dragon import *
import os





print("start time:",time.asctime(time.localtime()))
account = "zty001"
level = "泥块"
p = ""
num = 1
server = 'qa'







# item = items()
pat = os.getcwd()
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
table = open("{pat}\\MagicalCreaturesTemplate.csv".format(pat=pat),'r',encoding="utf-8-sig")
log_res = login_gm(server)                      #��¼GMƽ̨
info = get_playerid(account, log_res,server)    #��ȡplayerId
player = info['playerid']
session = info['sessionid']

for line in table:
    line_l = line.split(",")
    if line_l[0] == '':
        break
    if "{level}".format(level=level) in line_l[3] and "icon_dragon_attribute{p}".format(p=p) in line_l[10]:
        result = send_gift(line_l[0], num, player,session, account, log_res,server)
        print(line_l[0],line_l[3], num,result)
# send_gift(14001, 1, player,session, account, log_res,server)
# send_gift(2100, 1000, player,session, account, log_res,server)
# send_gift(2008, 1000, player,session, account, log_res,server)
# send_gift(7005, 1000, player,session, account, log_res,server)
# # send_gift(27500, 1, player,session, account, log_res,server)
send_gift(1001, 10000, player,session, account, log_res,server)
# table.close()
print("playerid:-{player}\nMission Completed!".format(player=player))



# %%


# 60ACB6F3-8CC3-4BDA-910E-7A56B5B5C2F9
# 60ACB6F3-8CC3-4BDA-910E-7A56B5B5C2F9