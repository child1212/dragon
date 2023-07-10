#%%
import os
pack_pos = os.path.dirname(os.path.dirname(__file__))
import sys
sys.path.append('{pack_pos}\\function'.format(pack_pos=pack_pos))
sys.path.append('{pack_pos}\\package'.format(pack_pos=pack_pos))
import time
from func_dragon import *
import pandas
import os

print("start time:",time.asctime(time.localtime()))
account = "799"
server = "ntest"                           
item_type = {36}
hat_types = {2,3,4}
'''
2:女主皮肤
4:帽子
'''
# item = items()



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

pat = os.path.dirname(__file__)
table = pandas.read_excel("E:\\FA\\nfa-config\\excel\\DataFile\\ItemTemplate.xlsx")
skins = table.values
log_res = login_gm(server)                      #��¼GMƽ̨
info = get_playerid(account, log_res,server)    #��ȡplayerId
player = info['playerid']
session = info['sessionid']

for line in skins:
    if line[7] in item_type:
        hatid = eval(line[26])[0]
        drawingtype = (hatid % 90000)//1000
        if drawingtype in hat_types:
            result = send_gift(line[0], 1, player,session, account, log_res,server)
            print(line[0],line[1], result)

            


# send_gift(1001, 100000, player,session, account, log_res,server)
# send_gift(1003, -100000, player,session, account, log_res,server)
print("playerid:-{player}\nMission Completed!".format(player=player))




# %%
