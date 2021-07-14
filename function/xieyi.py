#%%
import  sys
sys.path.append('D:\\pyprogram\\PyTestTools\\dragon\\package')
import time
import requests
import CoreModuleMsg_pb2  #登录、进入游戏、引导
import GatewayModuleMsg_pb2#结构
import TaskModuleMsg_pb2    #任务跳过

def protocol_post(requestId, server, **kwargs):
    if requestId == "1001":
        login()
    elif requestId == "1002":
        enterGame()
    elif requestId == "1005":
        completeGuide()
    elif requestId == "10001":
        taskComplete()
    elif requestId == "10004":
        skipTask()
    elif requestId == "25302":
        obstacleClear()

#登录
def login():
    request = GatewayModuleMsg_pb2.GatewayPackageRequest()
    msgBody = CoreModuleMsg_pb2.LoginRequest()
    msgBody.type = 
    msgBody.account = 
    msgBody.osType = 
    msgBody.idfa = 
    msgBody.idfv =
    msgBody.deviceId =
    msgBody.deviceCountry = 
    msgBody.adsGroup = 
    msgBody.platformType = 
    msg = msgBody.SerializeToString()
    request.senderId = 
    request.sessionId = 
    struct = request.bodys.add()
    struct.code = 
    struct.msgId = 
    struct.msgBody = 
    struct.genTime = 
    struct.sequenceId =
    struct.version = 
    
#进入游戏
def enterGame():
    pass

#完成引导
def completeGuide():
    pass

# 完成任务
def taskComplete():
    pass

#跳过任务
def skipTask():
    pass

#清除障碍
def obstacleClear():
    pass
