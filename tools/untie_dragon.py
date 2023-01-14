#%%
import sys
sys.path.append('D:\\pyprogram\\PyTestTools\\dragon\\function')
from func_dragon import *

server = "qa"                               #服务器前缀<dev:"tlogin", qa:"qausa">  #

if server == "38":
    server = "http://dtest.gameyici.com"
elif server == "qa":
    server = "https://dqa.hphorse.net"


log_res = login_gm(server)                      #登录GM平台
# accounts = ["e7f31a3db7b2446589eb37d053caba3e","C71519CC-15DB-44AB-BE21-757A097E0408","525C2D50-E9CD-47E9-B16F-1A33EF6F5FAA","603681214128417","000067.d4af54257490488293d8ab084d967d03.0422","e7f31a3db7b2446589eb37d053caba3e"]
accounts = ["525C2D50-E9CD-47E9-B16F-1A33EF6F5FAA","C71519CC-15DB-44AB-BE21-757A097E0408","B24C5797-BFE3-4FCE-8FA5-852FBEE63BC2"]
# accounts = ["525C2D50-E9CD-47E9-B16F-1A33EF6F5FAA","C71519CC-15DB-44AB-BE21-757A097E0408","5707B1FB-CFAA-4098-AC9D-842FAFCC8B32"]
# accounts = ["241DC209-EC71-44C0-98DF-D53ABC855812"]
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
