#%%
import sys
sys.path.append('D:\\pyprogram\\PyTestTools\\dragon\\package')
sys.path.append('D:\\pyprogram\\PyTestTools\\dragon\\function')
from func_dragon import *
from xieyi import *
import GatewayModuleMsg_pb2
import CoreModuleMsg_pb2
import GMModuleMsg_pb2
import time
import requests


task_dist = {}
task_dist["city"] = "gmSubmitTask city MIssion1_002StoreStuff"
task_dist["2"] = "gmSubmitTask 2 Mission1_013Outofcontroldragon"
task_dist["3"] = "gmSubmitTask 3 Mission2_012Themyteriousentrance"
task_dist["4"] = "gmSubmitTask 4 Mission3_011Arrangedragon"
task_dist["5"] = "gmSubmitTask 5 Mission4_013Newdiscovery"
task_dist["6"] = "gmSubmitTask 6 Mission6_017LockedDoor"
task_dist["7"] = "gmSubmitTask 7 Mission7_014Findthecanyon"
task_dist["8"] = "gmSubmitTask 8 Mission8_013TheDock"
task_dist["9"] = "gmSubmitTask 9 Mission9_014TheGateAboveStairs"

account = "903"
server = "http://dtest.gameyici.com" 
version = "9.1.0"
scene = "city"#input("输入地图编号")
cmd = task_dist[scene]
dragon = input("输入任意字符发龙！") #是否发龙

log = login(account,server,version)
entergame(log,server,version)
GM = GM_cmd(log,server,version,cmd)
print("任务跳转成功", cmd)
#发道具
log_res = login_gm(server) 
info = get_playerid(account, log_res,server)    #��ȡplayerId
player = info['playerid']
session = info['sessionid']
if dragon:
    send_gift(14052, 1, player,session, account, log_res,server)
    print("龙已发送")
else:
    send_gift(1001, 10000, player,session, account, log_res,server)
    print("奖励已发送")

guides = open("D:\\pyprogram\\PyTestTools\\dragon\\tools\\new_guide.txt","r",encoding="utf-8")

for line in guides:
    guide = line.replace("\n","")
    skip_guide(log,server,version,guide)
    print(line)
guides.close()


# %%
