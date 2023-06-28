import time
import requests
import json
import os
pack_pos = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
import sys
sys.path.append('{pack_pos}\\function'.format(pack_pos=pack_pos))
from func_dragon import *
from xieyi import *


class player_data:
    def __init__(self,playerInfo) -> None:
        self.msg = playerInfo.get("msg")
        self.code = playerInfo.get("code")
        self.page = playerInfo.get("page")
        self.playerid = playerInfo.get("playerId")
        self.allData = {}
        for i in self.page.get("list"):
            self.allData[i["key"]] = i["value"]

class ActiveEgg:
    def __init__(self,player_data) -> None:
        self.key = 'P{playerid}@{{{playerid}}}-ActiveEgg'.format(playerid=player_data.playerid)
        self.value = player_data.allData.get(self.key)
        self.data = json.loads(self.value)

class Properties:
    def __init__(self,player_data) -> None:
        self.key = 'P{playerid}@{{{playerid}}}-Properties'.format(playerid=player_data.playerid)
        self.value = player_data.allData.get(self.key)
        self.data = json.loads(self.value)

class GrowthFund:
    def __init__(self,player_data) -> None:
        self.key = 'P{playerid}@{{{playerid}}}-GrowthFund'.format(playerid=player_data.playerid)
        self.value = player_data.allData.get(self.key)
        self.data = json.loads(self.value)

class Mail:
    def __init__(self,player_data) -> None:
        self.key = 'P{playerid}@{{{playerid}}}-Mail'.format(playerid=player_data.playerid)
        self.value = player_data.allData.get(self.key)
        self.data = json.loads(self.value)

class Activity:
    def __init__(self,player_data) -> None:
        self.key = 'P{playerid}@{{{playerid}}}-Activity'.format(playerid=player_data.playerid)
        self.value = player_data.allData.get(self.key)
        self.data = json.loads(self.value)

class Ads:
    def __init__(self,player_data) -> None:
        self.key = 'P{playerid}@{{{playerid}}}-Ads'.format(playerid=player_data.playerid)
        self.value = player_data.allData.get(self.key)
        self.data = json.loads(self.value)

class OrderTask:
    def __init__(self,player_data) -> None:
        self.key = 'P{playerid}@{{{playerid}}}-OrderTask'.format(playerid=player_data.playerid)
        self.value = player_data.allData.get(self.key)
        self.data = json.loads(self.value)

class MagicalCreature:
    def __init__(self,player_data) -> None:
        self.key = 'P{playerid}@{{{playerid}}}-MagicalCreature'.format(playerid=player_data.playerid)
        self.value = player_data.allData.get(self.key)
        self.data = json.loads(self.value)

        
#%%
def change_Param(classname,login_res,host,params):
    '''
    info:player_data(playerinfo).allData,总数据
    playerid :　player_data(playerinfo).playerid
    params : 子类.data
    name : 子类名称
    '''
    key = classname.key
    value = classname.value
    value = json.loads(value)
    for i in params:
        value[i] = params[i]
    value = json.dumps(value)    

    url_itemlist = "{host}/BI/bi/bieditplayerdata/update".format(host=host)
    data_itemlist = '{"rowKey":"","rowValue":"","note":null,"serverId":null}'
    data_itemlist = json.loads(data_itemlist)
    data_itemlist["rowKey"] = key
    data_itemlist["rowValue"] = value
    data_itemlist = json.dumps(data_itemlist)

    headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
    "Content-Type": "application/json",
    "Origin": "{host}".format(host=host),
    "Referer": "{host}/BI/modules/bi/biqatool.html".format(host=host),
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    }

    res_item = requests.post(url_itemlist, data=data_itemlist,cookies = login_res.cookies, headers=headers)
    res_list = res_item.text
    res_list = json.loads(res_list)
    return res_list
    
#%%
# %%
