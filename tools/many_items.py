
#%%
import os
pack_pos = os.path.dirname(os.path.dirname(__file__))
import sys
sys.path.append('{pack_pos}\\function'.format(pack_pos=pack_pos))
sys.path.append('{pack_pos}\\package'.format(pack_pos=pack_pos))
import time
from func_dragon import *
import pandas as pd
print("start time:",time.asctime(time.localtime()))
account = "799"
num = 2000
server = "ntest"    
project = "NFA"                       
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

if project == "DFA":
    file_path = "E:\\dragon\\dragon-config\\excel\\DataFile"
    table = pd.read_excel("{file_path}\\ItemTemplate.xlsx".format(file_path=file_path))

if project == "NFA":
    file_path = "E:\\FA\\nfa-config\\excel\\DataFile"
    table = pd.read_excel("{file_path}\\ItemTemplate.xlsx".format(file_path=file_path))

log_res = login_gm(server)                      #��¼GMƽ̨
info = get_playerid(account, log_res,server)    #��ȡplayerId
player = info['playerid']
session = info['sessionid']
item_type = (2,3,5,7,13,15,16,18,25,32)

# for item in range(2020,2032):
#     send_gift(item, 10, player,session, account, log_res,server)
data = table.values
for i in range(3,len(data)):
    if not pd.isna(data[i][1]) and not pd.isna(data[i][4]) and "龙" not in data[i][1] and "icon4" not in data[i][4] and "icon5" not in data[i][4]:
        if int(data[i][7]) in item_type:
            result = send_gift(data[i][0], num, player,session, account, log_res,server)
            print(data[i][0],data[i][1], num,result)


send_gift(1001, 100000, player,session, account, log_res,server)
send_gift(1003, 100, player,session, account, log_res,server)
print("playerid:-{player}\nMission Completed!".format(player=player))




# %%
