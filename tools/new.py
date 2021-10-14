#%%
import sys
sys.path.append('D:\\pyprogram\\PyTestTools\\dragon\\package')
sys.path.append('D:\\pyprogram\\PyTestTools\\dragon\\function')
from func_dragon import *
import GatewayModuleMsg_pb2
import CoreModuleMsg_pb2
import GMModuleMsg_pb2
import time
import requests


def login(account,server,version):
    request = GatewayModuleMsg_pb2.GatewayPackageRequest()
    msgbody = CoreModuleMsg_pb2.LoginRequest()
    resa = GatewayModuleMsg_pb2.GatewayPackageResponse()
    res_1001 = CoreModuleMsg_pb2.LoginResponse()
    request.senderId = "VISITOR"
    request.sessionId = 0
    msgbody.type = 0
    msgbody.account = str(account)
    msgbody.visitorAccount = "2"
    msgbody.osType = 0
    msgbody.platformType = 0
    # msgbody.idfa = "A91E6759-4AF3-43B7-B91D-EBCC2F2C7C07 "
    msgbody.deviceCountry = "00"
    # msgbody.deviceId = "241DC209-EC71-44C0-98DF-D53ABC855812"
    # msgbody.idfv = "E9D28AB3-4B1F-42F4-87F9-E9EED4C98AE2"
    msg = msgbody.SerializeToString()
    struct = request.bodys.add()
    struct.code = 0
    struct.msgId =1001
    struct.msgBody = msg
    struct.genTime = int(time.time()*1000)
    struct.sequenceId = 0
    struct.version = version
    url = "{server}/{version}?id=1001&uid=VISITOR&ver={version}".format(server=server, version=version)
    response = requests.put(url,data=request.SerializeToString())
    if response.status_code==200 : 
        resa.ParseFromString(response.content)
        res_1001.ParseFromString(resa.bodys[0].msgBody)
        print("playerid:",res_1001.playerId)
        return res_1001
    else:
        print("Server Disconnected ！！!")
        return 0


def entergame(login_res,server,version):
    request = GatewayModuleMsg_pb2.GatewayPackageRequest()
    msgbody = CoreModuleMsg_pb2.EnterGameRequest()
    resa = GatewayModuleMsg_pb2.GatewayPackageResponse()
    # res_1002 =CoreModuleMsg_pb2.EnterGameResponse()
    request.senderId = login_res.playerId
    request.sessionId = login_res.sessionId
    msgbody.flag = True
    msg = msg = msgbody.SerializeToString()
    struct = request.bodys.add()
    struct.code = 0
    struct.msgId =1002
    struct.msgBody = msg
    struct.genTime = int(time.time()*1000)
    struct.sequenceId = 0
    struct.version = version
    url = "{server}/{version}?id=1002&uid=VISITOR&ver={version}".format(server=server, version=version)
    response = requests.put(url,data=request.SerializeToString())
    if response.status_code==200 : 
        resa.ParseFromString(response.content)
        # res_1002.ParseFromString(resa.bodys[0].msgBody)
        return resa
    else:
        print("Server Disconnected ！！!")
        return 0


def GM_cmd(login_res,server,version,cmd):
    request = GatewayModuleMsg_pb2.GatewayPackageRequest()
    msgbody = GMModuleMsg_pb2.GMCommandRequest()
    resa = GatewayModuleMsg_pb2.GatewayPackageResponse()
    res_100 = GMModuleMsg_pb2.GMCommandResponse()
    request.senderId = login_res.playerId
    request.sessionId = login_res.sessionId
    msgbody.cmd = cmd
    msg = msg = msgbody.SerializeToString()
    struct = request.bodys.add()
    struct.code = 0
    struct.msgId =100
    struct.msgBody = msg
    struct.genTime = int(time.time()*1000)
    struct.sequenceId = 0
    struct.version = version
    url = "{server}/{version}?id=100&uid=VISITOR&ver={version}".format(server=server, version=version)
    response = requests.put(url,data=request.SerializeToString())
    if response.status_code==200 : 
        resa.ParseFromString(response.content)
        res_100.ParseFromString(resa.bodys[0].msgBody)
        print(resa)
        return resa
    else:
        print("Server Disconnected ！！!")
        return 0

account = "798"
server = "http://dtest.gameyici.com" 
version = "7.1.0"
cmd = "gmSubmitTask 3 Mission2_012Themyteriousentrance"


log = login(account,server,version)
entergame(log,server,version)
GM = GM_cmd(log,server,version,cmd)

#发沙石龙
log_res = login_gm(server) 
info = get_playerid(account, log_res,server)    #��ȡplayerId
player = info['playerid']
session = info['sessionid']
send_gift(14052, 1, player,session, account, log_res,server)

# %%
