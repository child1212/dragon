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
accounts = {
    "mm0600",
    "mm0601"
}
item_id = "1003"
num = -300
server = "nqa"                           
# item = items()



if server == "ntest":
    server = "https://nfa-test.bettagames.com"
elif server == "nqa":
    server = "https://qa-nfa.hphorse.net"
# elif server == "nrelease":
#     server = "https://online-nfa.hphorse.net"
elif server == "38":
    server = "http://dtest.gameyici.com"
elif server == "qa":
    server = "https://dqa.hphorse.net"
# elif server == "dragon":
#     server = "https://dragon.hphorse.net"
elif server == "act":
    server = "http://dact.gameyici.com"


pat = os.path.dirname(os.path.abspath(__file__))
table = open("{pat}\\ItemTemplate.csv".format(pat=pat),'r',encoding='utf-8')
log_res = login_gm(server)                      #��¼GMƽ̨
for account in accounts:
    info = get_playerid(account, log_res,server)    #��ȡplayerId
    player = info['playerid']
    session = info['sessionid']

    send_gift(item_id,num, player,session, account, log_res,server)
