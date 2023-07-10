#%%
import time
import requests
import json
import copy
import os
pack_pos = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
import sys
sys.path.append('{pack_pos}\\function'.format(pack_pos=pack_pos))
from func_dragon import *
from xieyi import *
from player_data import *
param = {}
class MagicalCreature_class:
    def __init__(self,account,server):
        self.account = account
        self.server = server
        self.log_res = login_gm(server)
        self.res = get_playerid(self.account,self.log_res,self.server)
        self.player = self.res["playerid"]
        self.playerinfo =  get_player_info(self.account,self.player,self.server,self.log_res)
        self.skins_info = {}
        self.partners_info = {}
        self.skins = set()
        self.partners = set()
        self.skin_new_dict = {}
        self.skin_lost_dict = {}
        self.partners_lost_dict = {}
        self.partners_new_dict = {}

    def update(self):
        prop = MagicalCreature(player_data(self.playerinfo)).data
        skins_info = prop.get('skins')
        partners_info = prop.get('creatures')
        skins = set(skins_info.keys())
        partners = set(partners_info.keys())
        #皮肤新增
        skin_new = skins-self.skins
        self.skin_new_dict = {}
        for skin in skin_new:
            self.skin_new_dict[skin] = skins_info[skin]
        #皮肤减少
        skin_lost = self.skins-skins
        self.skin_lost_dict = {}
        for skin in skin_lost:
            self.skin_lost_dict[skin] = self.skins_info[skin]
        #生物新增
        partners_lost = self.partners - partners
        self.partners_lost_dict = {}
        for partner in partners_lost:
            self.partners_lost_dict[partner] = self.partners_info[partner]
        #生物减少
        partners_new = partners - self.partners
        self.partners_new_dict = {}
        for partner in partners_new:
            self.partners_new_dict[partner] = partners_info[partner]
        #更新数据
        self.skins = skins
        self.partners = partners
        self.skins_info = skins_info
        self.partners_info = partners_info

    def dump_changes(self):
        print("新增帽子：")
        for k in self.skin_new_dict:
            print(self.skin_new_dict[k].get('tplId'))
        print("丢失帽子：")
        for k in self.skin_lost_dict:
            print(self.skin_lost_dict[k].get('tplId'))
        print("丢失伙伴：")
        for k in self.partners_lost_dict:
            print(self.partners_lost_dict[k].get('templateId'))
        print("新增伙伴：")
        for k in self.partners_new_dict:
            print(self.partners_new_dict[k].get('templateId'))

#################################################
server = "38"
account = input("account:")




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



a = MagicalCreature_class(account,server)
running = ''
while running == '':
    a.update()
    a.dump_changes()
    running = input("continue:")


#%%



