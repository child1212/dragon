#%%
import sys
sys.path.append('D:\\pyprogram\\PyTestTools\\dragon\\function')
import time
from func_dragon import *
import os

print("start time:",time.asctime(time.localtime()))
account = "16dfe5819d850f195c79d3db04f4bbfa"
player = "ojeha8"
server = "https://dqa.gameyici.com"      
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