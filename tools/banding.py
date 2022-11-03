#%%
import sys
sys.path.append('D:\\pyprogram\\PyTestTools\\dragon\\function')
import time
from func_dragon import *
import os

print("start time:",time.asctime(time.localtime()))
account = "hc123"
player = "ureyno"
server = "38"      




if server == "38":
    server = "http://dtest.gameyici.com"
elif server == "qa":
    server = "https://dqa.hphorse.net"
elif server == "act":
    server = "http://dact.gameyici.com"

log_res = login_gm(server)    
fin = banding(account,player,server,log_res)

print(account,player,fin)



#%%
#以下是批量绑定
import sys
sys.path.append('D:\\pyprogram\\PyTestTools\\dragon\\function')
import time
from func_dragon import *
import os
dic = dict()
dic["swd20"] = "swd20"
dic["swd21"] = "swd21"
dic["swd22"] = "swd22"
dic["swd23"] = "swd23"
dic["swd24"] = "swd24"
dic["swd25"] = "swd25"
dic["swd26"] = "swd26"
dic["swd27"] = "swd27"
dic["swd28"] = "swd28"
dic["swd29"] = "swd29"
dic["swd30"] = "swd30"
dic["swd31"] = "swd31"
server = "qa"      

if server == "38":
    server = "http://dtest.gameyici.com"
elif server == "qa":
    server = "https://dqa.hphorse.net"
elif server == "act":
    server = "http://dact.gameyici.com"
log_res = login_gm(server)  

print("start time:",time.asctime(time.localtime()))
for key in dic:
    account = key
    player = dic[key]
    fin = banding(account,player,server,log_res)
    print(account,player,fin)
# %%
