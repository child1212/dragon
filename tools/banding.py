#%%
import sys
sys.path.append('D:\\pyprogram\\PyTestTools\\dragon\\function')
import time
from func_dragon import *
import os

print("start time:",time.asctime(time.localtime()))
account = "3fd3616289c03b6df77b85dae95dabfc"
player = "53ij9m"
server = "qa"      




if server == "38":
    server = "http://dtest.gameyici.com"
elif server == "qa":
    server = "https://dqa.hphorse.net"
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
dic["89759f09f4aacecba561cf402a05152d"] = "pvhui5"
dic["A2A90680-DAF1-4C12-8DAE-F814635F1839"] = "hpvkq"
dic["5AD6D528-ABEF-4D6F-ACC8-E3782EF85228"] = "ojehaq"
server = "http://dtest.gameyici.com"      

log_res = login_gm(server)  
print("start time:",time.asctime(time.localtime()))
for key in dic:
    account = key
    player = dic[key]
    fin = banding(account,player,server,log_res)
    print(account,player,fin)
# %%
