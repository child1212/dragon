#%%
import sys
sys.path.append('D:\\pyprogram\\PyTestTools\\dragon\\package')
import time
import requests
import CoreModuleMsg_pb2  #登录、进入游戏、引导
import GatewayModuleMsg_pb2#结构
import GMModuleMsg_pb2
import ChatModuleMsg_pb2
import TeamModuleMsg_pb2
import VipModuleMsg_pb2

#登录#1001
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
    msgbody.osType = 1
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
        return res_1001
    else:
        print("Server Disconnected ！！!")
        return 0

#进入游戏#1002
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

#使用GM指令
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


#跳引导
def skip_guide(login_res,server,version,guideId):
    request = GatewayModuleMsg_pb2.GatewayPackageRequest()
    msgbody = CoreModuleMsg_pb2.GuideCompleteRequest()
    resa = GatewayModuleMsg_pb2.GatewayPackageResponse()
    res_100 = CoreModuleMsg_pb2.GuideCompleteResponse()
    request.senderId = login_res.playerId
    request.sessionId = login_res.sessionId
    msgbody.guideId = guideId
    msg = msgbody.SerializeToString()
    struct = request.bodys.add()
    struct.code = 0
    struct.msgId =1005
    struct.msgBody = msg
    struct.genTime = int(time.time()*1000)
    struct.sequenceId = 0
    struct.version = version
    url = "{server}/{version}?id=1005&uid=VISITOR&ver={version}".format(server=server, version=version)
    response = requests.put(url,data=request.SerializeToString())
    if response.status_code==200 : 
        resa.ParseFromString(response.content)
        res_100.ParseFromString(resa.bodys[0].msgBody)
        print(resa)
        return resa
    else:
        print("Server Disconnected ！！!")
        return 0

def chat_message(login_res,server,version,cid,message,data_1002):
    '''
    login_res:1001返回数据
    server:服务器
    version:版本号
    cid:公会id
    message:信息内容
    data_1002:解码后的1002数据
    '''
    request = GatewayModuleMsg_pb2.GatewayPackageRequest()
    msgbody = ChatModuleMsg_pb2.ChatRequest()
    resa = GatewayModuleMsg_pb2.GatewayPackageResponse()
    # chatinfo = ChatModuleMsg_pb2.ChatInfo()
    res_100 = ChatModuleMsg_pb2.ChatResponse()
    request.senderId = login_res.playerId
    request.sessionId = login_res.sessionId
    msgbody.chatInfo.pid = login_res.playerId
    msgbody.chatInfo.pname = data_1002.resourceMsg.nickName
    msgbody.chatInfo.head = data_1002.resourceMsg.icon
    msgbody.chatInfo.frame = data_1002.playerInfoResp.frame
    msgbody.chatInfo.timeStamp = 0
    msgbody.chatInfo.content = message
    msgbody.chatInfo.title = ""
    msgbody.cid = cid
    msg = msgbody.SerializeToString()
    struct = request.bodys.add()
    struct.code = 0
    struct.msgId = 27301
    struct.msgBody = msg
    struct.genTime = int(time.time()*1000)
    struct.sequenceId = 0
    struct.version = version
    url = "{server}/chat/{version}?id=27301_&uid={pid}".format(server=server, version=version, pid=login_res.playerId)
    response = requests.put(url,data=request.SerializeToString())
    if response.status_code==200 : 
        resa.ParseFromString(response.content)
        res_100.ParseFromString(resa.bodys[0].msgBody)
        return resa
    else:
        print("Server Disconnected ！！!")
        return 0

def team_need_help(login_res,server,version,cid,itemid):
    '''
    login_res:1001返回数据
    server:服务器
    version:版本号
    cid:公会id
    itemid:道具id
    '''
    request = GatewayModuleMsg_pb2.GatewayPackageRequest()
    msgbody = TeamModuleMsg_pb2.TeamNeedHelpRequest()
    resa = GatewayModuleMsg_pb2.GatewayPackageResponse()
    res_100 = TeamModuleMsg_pb2.TeamNeedHelpResponse()
    request.senderId = login_res.playerId
    request.sessionId = login_res.sessionId
    msgbody.teamId = cid
    msgbody.templateId = itemid
    msg = msgbody.SerializeToString()
    struct = request.bodys.add()
    struct.code = 0
    struct.msgId =27011
    struct.msgBody = msg
    struct.genTime = int(time.time()*1000)
    struct.sequenceId = 0
    struct.version = version
    url = "{server}/game/{version}?id=27011&uid={pid}".format(server=server, version=version, pid=login_res.playerId)
    response = requests.put(url,data=request.SerializeToString())
    if response.status_code==200 : 
        resa.ParseFromString(response.content)
        res_100.ParseFromString(resa.bodys[0].msgBody)
        return resa
    else:
        print("Server Disconnected ！！!")
        return 0

def join_team(login_res,server,version,cid):
    '''
    login_res:1001返回数据
    server:服务器
    version:版本号
    cid:公会id
    '''
    request = GatewayModuleMsg_pb2.GatewayPackageRequest()
    msgbody = TeamModuleMsg_pb2.JoinTeamRequest()
    resa = GatewayModuleMsg_pb2.GatewayPackageResponse()
    res_100 = TeamModuleMsg_pb2.JoinTeamResponse()
    request.senderId = login_res.playerId
    request.sessionId = login_res.sessionId
    msgbody.id = cid
    msg = msgbody.SerializeToString()
    struct = request.bodys.add()
    struct.code = 0
    struct.msgId =27002
    struct.msgBody = msg
    struct.genTime = int(time.time()*1000)
    struct.sequenceId = 0
    struct.version = version
    url = "{server}/game/{version}?id=27002&uid={pid}".format(server=server, version=version, pid=login_res.playerId)
    response = requests.put(url,data=request.SerializeToString())
    if response.status_code==200 : 
        resa.ParseFromString(response.content)
        res_100.ParseFromString(resa.bodys[0].msgBody)
        print(resa)
        return resa
    else:
        print("Server Disconnected ！！!")
        return 0


def leave_team(login_res,server,version,cid):
    '''
    login_res:1001返回数据
    server:服务器
    version:版本号
    cid:公会id
    '''
    request = GatewayModuleMsg_pb2.GatewayPackageRequest()
    msgbody = TeamModuleMsg_pb2.QuitTeamRequest()
    resa = GatewayModuleMsg_pb2.GatewayPackageResponse()
    res_100 = TeamModuleMsg_pb2.QuitTeamResponse()
    request.senderId = login_res.playerId
    request.sessionId = login_res.sessionId
    msgbody.id = cid
    msg = msgbody.SerializeToString()
    struct = request.bodys.add()
    struct.code = 0
    struct.msgId =27003
    struct.msgBody = msg
    struct.genTime = int(time.time()*1000)
    struct.sequenceId = 0
    struct.version = version
    url = "{server}/game/{version}?id=27003&uid={pid}".format(server=server, version=version, pid=login_res.playerId)
    response = requests.put(url,data=request.SerializeToString())
    if response.status_code==200 : 
        resa.ParseFromString(response.content)
        res_100.ParseFromString(resa.bodys[0].msgBody)
        print(resa)
        return resa
    else:
        print("Server Disconnected ！！!")
        return 0


def get_vip(login_res,server,version):
    '''
    login_res:1001返回数据
    server:服务器
    version:版本号
    cid:公会id
    '''
    request = GatewayModuleMsg_pb2.GatewayPackageRequest()
    msgbody = VipModuleMsg_pb2.VipInfoRequest()
    resa = GatewayModuleMsg_pb2.GatewayPackageResponse()
    res_100 = VipModuleMsg_pb2.VipInfoResponse()
    request.senderId = login_res.playerId
    request.sessionId = login_res.sessionId
    msg = msgbody.SerializeToString()
    struct = request.bodys.add()
    struct.code = 0
    struct.msgId =28801
    struct.msgBody = msg
    struct.genTime = int(time.time()*1000)
    struct.sequenceId = 0
    struct.version = version
    url = "{server}/game/{version}?id=28801&uid={pid}".format(server=server, version=version, pid=login_res.playerId)
    response = requests.put(url,data=request.SerializeToString())
    if response.status_code==200 : 
        resa.ParseFromString(response.content)
        res_100.ParseFromString(resa.bodys[0].msgBody)
        print(resa)
        return resa
    else:
        print("Server Disconnected ！！!")
        return 0