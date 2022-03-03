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


account = "1403"
server = "38"
version = "14.1.0"
scene = "12"#input("输入地图编号")




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
task_dist["13"] = "Mission13_014TrueHeart"
task_dist["14"] = "Mission14_015ThePortalDoor"



if server == "38":
    server = "http://dtest.gameyici.com"
elif server == "qa":
    server = "https://dqa.hphorse.net"
cmd = task_dist[scene]
dragon = "1"#input("输入任意字符发龙！") #是否发龙

log = login(account,server,version)
entergame(log,server,version)
GM = GM_cmd(log,server,version,cmd)
print("任务跳转成功", cmd)
#发道具
log_res = login_gm(server) 
info = get_playerid(account, log_res,server)    #��ȡplayerId
player = info['playerid']
session = info['sessionid']
# send_gift(14054, 1, player,session, account, log_res,server)
# send_gift(27201, 1, player,session, account, log_res,server)
# send_gift(27101, 1, player,session, account, log_res,server)
# send_gift(27102, 1, player,session, account, log_res,server)

guides = open("D:\\pyprogram\\PyTestTools\\dragon\\tools\\new_guide.txt","r",encoding="utf-8")

for line in guides:
    guide = line.replace("\n","")
    skip_guide(log,server,version,guide)
    print(line)
guides.close()
send_gift(1002, 10000, player,session, account, log_res,server)
send_gift(1001, 10000, player,session, account, log_res,server)

print("finish")



# %%
