#%%
import os
pack_pos = os.path.dirname(os.path.dirname(__file__))
import sys
sys.path.append('{pack_pos}\\function'.format(pack_pos=pack_pos))
sys.path.append('{pack_pos}\\package'.format(pack_pos=pack_pos))
from func_dragon import *
from xieyi import *
import GatewayModuleMsg_pb2
import CoreModuleMsg_pb2
import GMModuleMsg_pb2
import time
import requests

# account ="525C2D50-E9CD-47E9-B16F-1A33EF6F5FAA"
# account = "e7f31a3db7b2446589eb37d053caba3e"
# account = "C71519CC-15DB-44AB-BE21-757A097E0408"
# account = "DBFABEFD-A297-4C48-B94E-4EC185B6AEE3"
account = "4101"

server = "qa"
version = "41.1.0"
scene = "2"#input("输入地图编号")
skip = 0



def new(account,server,version,scene,skip):
    task_dist = {}
    task_dist["city"] = "gmSubmitTask city MIssion1_002StoreStuff"
    task_dist["2"] = "gmSubmitTask 2 Mission1_013Outofcontroldragon"
    task_dist["3"] = "gmSubmitTask 3 Mission2_012Themyteriousentrance"
    task_dist["4"] = "gmSubmitTask 4 Mission3_0010Theotherdragonnest"
    task_dist["5"] = "gmSubmitTask 5 Mission4_013Newdiscovery"
    task_dist["6"] = "gmSubmitTask 6 Mission6_017LockedDoor"
    task_dist["7"] = "gmSubmitTask 7 Mission7_014Findthecanyon"
    task_dist["8"] = "gmSubmitTask 8 Mission8_013TheDock"
    task_dist["9"] = "gmSubmitTask 9 Mission9_014TheGateAboveStairs"
    task_dist["10"] = "gmSubmitTask 10 Mission10_009EntrancetotheForbiddenLand"
    task_dist["11"] = "gmSubmitTask 11 Mission11_009TrialEntrance"
    task_dist["12"] = "gmSubmitTask 12 Mission12_012TeleportationPortal"
    task_dist["13"] = "gmSubmitTask 13 Mission13_014TrueHeart"
    task_dist["14"] = "gmSubmitTask 14 Mission14_015ThePortalDoor"
    task_dist["15"] = "gmSubmitTask 15 Mission15_014WisdomFeedback"
    task_dist["16"] = "gmSubmitTask 16 Mission16_014DragonBlessing"
    task_dist["17"] = "gmSubmitTask 17 Mission17_012Conchchannel"
    task_dist["18"] = "gmSubmitTask 18 Mission18_012Mysteriousmine"
    task_dist["19"] = "gmSubmitTask 19 Mission19_012Endofthemine"
    task_dist["20"] = "gmSubmitTask 20 Mission20_013Unknownahead"
    task_dist["21"] = "gmSubmitTask 21 Mission21_013ShiresTreasure"



    if server == "38":
        server = "http://dtest.gameyici.com"
    elif server == "qa":
        server = "https://dqa.hphorse.net"
    elif server == "act":
        server = "http://dact.gameyici.com"

    cmd = task_dist[scene]

    log = login(account,server,version)
    entergame(log,server,version)
    GM = GM_cmd(log,server,version,cmd)
    print("任务跳转成功", cmd)
    #发道具
    log_res = login_gm(server) 
    info = get_playerid(account, log_res,server)    #��ȡplayerId
    player = info['playerid']
    session = info['sessionid']
    # send_gift(1001, 9999, player,session, account, log_res,server)
    # send_gift(6000, 200, player,session, account, log_res,server)
    # send_gift(27101, 1, player,session, account, log_res,server)
    # send_gift(27102, 1, player,session, account, log_res,server)

    guides = open("E:\\PyTools\\dragon\\tools\\new_guide.txt","r",encoding="utf-8")
    if skip == 1:
        for line in guides:
            guide = line.replace("\n","")
            skip_guide(log,server,version,guide)
            print(line)
        guides.close()

    # send_gift(1002, 10000, player,session, account, log_res,server)
    # send_gift(1003, 100000, player,session, account, log_res,server)


    print(player,"-finish")

# for i in range(100, 200):
#     account = 'act{i}'.format(i=i)
new(account,server,version,scene,skip)

# %%
