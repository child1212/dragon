#%%
import os
pack_pos = os.path.dirname(os.path.dirname(__file__))
import sys
sys.path.append('{pack_pos}\\function'.format(pack_pos=pack_pos))
sys.path.append('{pack_pos}\\package'.format(pack_pos=pack_pos))
from func_dragon import *

server = "qa"                               #服务器前缀<dev:"tlogin", qa:"qausa">  #

if server == "38":
    server = "http://dtest.gameyici.com"
elif server == "qa":
    server = "https://dqa.hphorse.net"
elif server == "nqa":
    server = "https://qa-nfa.hphorse.net"



log_res = login_gm(server)                      #登录GM平台
# accounts = ["e7f31a3db7b2446589eb37d053caba3e","C71519CC-15DB-44AB-BE21-757A097E0408","525C2D50-E9CD-47E9-B16F-1A33EF6F5FAA","603681214128417","000067.d4af54257490488293d8ab084d967d03.0422","e7f31a3db7b2446589eb37d053caba3e"]
# accounts = ["525C2D50-E9CD-47E9-B16F-1A33EF6F5FAA","C71519CC-15DB-44AB-BE21-757A097E0408","B24C5797-BFE3-4FCE-8FA5-852FBEE63BC2","68D0340C-53C6-4302-90D9-5685727FB559","FE63D781-B170-42DA-B823-6F9169743103"]
# accounts = ["525C2D50-E9CD-47E9-B16F-1A33EF6F5FAA","C71519CC-15DB-44AB-BE21-757A097E0408","5707B1FB-CFAA-4098-AC9D-842FAFCC8B32"]
# accounts = ["241DC209-EC71-44C0-98DF-D53ABC855812"]
accounts = ["13BB168D-2B67-43BB-A9A7-969ECD46F380"]
for i in accounts:
    try:
        account = "{n}".format(n=str(i))
        info = get_playerid(account, log_res,server)    #获取playerId
        player = info['playerid']
        session = info['sessionid']
        result = untie(player,session,account,log_res,server)
        print('解绑账号  {acc}  :  {p}{lue}{result}'.format(acc=account,p=player,result=result,lue="-"*(55-len(account)-len(player))))
    except:
        print('解绑账号  {acc}  {lue}没有该账号'.format(acc=account,lue="-"*(52-len(account))))
# %%
