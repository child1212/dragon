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
account = "onl796"
level = ""
attribute = ""
typ = []
# typ = {101}#nfa专属
num = 10
server = 'nqa'
project = "NFA"#DFA/NFA
group = 100







# item = items()
pat = os.path.dirname(__file__)

if server == "ntest":
    server = "http://192.168.1.143"
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

    table = pd.read_excel("{file_path}\\MagicalCreaturesTemplate.xlsx".format(file_path=file_path))
    log_res = login_gm(server)                      #
    info = get_playerid(account, log_res,server)    #
    player = info['playerid']
    session = info['sessionid']
    data = table.values
    x = 0
    for line in range(3,len(data)):
        if "{level}".format(level=level) in data[line,3] and "icon_dragon_attribute{p}".format(p=attribute) in data[line,10] and x <= group:
            result = send_gift(data[line,0], num, player,session, account, log_res,server)
            x += 1
            print(data[line,0],data[line,3], num,result)
running = 0
if project == "NFA":
    file_path = "E:\\FA\\nfa-config\\excel\\DataFile"
    table = pd.read_excel("{file_path}\\MagicalCreaturesTemplate.xlsx".format(file_path=file_path))
    log_res = login_gm(server)                      #
    info = get_playerid(account, log_res,server)    #
    player = info['playerid']
    session = info['sessionid']
    data = table.values
    x = 0
    for line in range(3,len(data)):
        # if data[line,0]-data[line,3]*1000 == 1:
        if data[line,0]-data[line,3]*1000 == 1 and x < group and data[line,3] > 0:
            if "{level}".format(level=level) in data[line,2]:
                if attribute == '' or data[line,10][1] == attribute:
                    if typ == [] or data[line,3] in typ:
                        result = send_gift(data[line,0], num, player,session, account, log_res,server)
                        x += 1
                        print(data[line,0],data[line,2], num,result)












# send_gift(14001, 1, player,session, account, log_res,server)
# send_gift(2100, 1000, player,session, account, log_res,server)
# send_gift(2008, 1000, player,session, account, log_res,server)
# send_gift(7005, 1000, player,session, account, log_res,server)
# # send_gift(27500, 1, player,session, account, log_res,server)
send_gift(1002, 10000000, player,session, account, log_res,server)
print("playerid:-{player}\nMission Completed!".format(player=player))




# %%


# 60ACB6F3-8CC3-4BDA-910E-7A56B5B5C2F9
# 60ACB6F3-8CC3-4BDA-910E-7A56B5B5C2F9