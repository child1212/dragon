#%%
import sys
sys.path.append('D:\\pyprogram\\PyTestTools\\dragon\\function')
import time
from func_dragon import *
import os



def get_item_num(itemid,log_res,player,server):
    info = get_accountid(player, log_res,server)  #获取playerId
    account = info["accountid"]
    session = info["sessionid"]
    # player = 'lc8b8r' 
    lis = get_itemlist(player,session,account,log_res,server)
    lis = eval(lis['item'])
    for infomation in lis:
        if infomation["id"] == str(itemid):
            return infomation["num"]




players = open('D:\\pyprogram\\PyTestTools\\dragon\\bug\\pidl.txt','r',encoding='utf-8-sig')
server = "https://dragon.hphorse.net"
item = 1001



for player in players:
    player = player.replace('\n','')
    log_res = login_gm(server)                      #登录GM平台
    count = get_item_num(item,log_res,player,server)
    print(player,':',count)
players.close()
# %%
