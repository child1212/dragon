#%%
import sys
sys.path.append('D:\\pyprogram\\PyTestTools\\dragon\\package')
import time
import requests
import CoreModuleMsg_pb2  #登录、进入游戏、引导
import GatewayModuleMsg_pb2#结构
import TaskModuleMsg_pb2    #任务跳过
import SceneModuleMsg_pb2
import OrderTaskModuleMsg_pb2
import FarmlandModuleMsg_pb2
import ItemModuleMsg_pb2
import MagicalCreatureModuleMsg_pb2

#登录
def login(account, server, version):
    request = GatewayModuleMsg_pb2.GatewayPackageRequest()
    msgBody = CoreModuleMsg_pb2.LoginRequest()
    res = GatewayModuleMsg_pb2.GatewayPackageResponse()
    res_1001 = CoreModuleMsg_pb2.LoginResponse()
    msgBody.type = 0
    msgBody.account = str(account)
    msgBody.osType = 1
    msgBody.idfa = "A91E6759-4AF3-43B7-B91D-EBCC2F2C7C07 "
    msgBody.idfv = "E9D28AB3-4B1F-42F4-87F9-E9EED4C98AE2"
    msgBody.deviceId = "241DC209-EC71-44C0-98DF-D53ABC855812"
    msgBody.deviceCountry = "zh_CN"
    # msgBody.adsGroup = '{"channel":"appsflyer","deviceid":"A91E6759-4AF3-43B7-B91D-EBCC2F2C7C07","attribution":{"is_first_launch":false,"install_time":"2021-03-2606:13:30.152","af_message":"organicinstall","af_status":"Organic"}}'
    msgBody.platformType = 0
    msg = msgBody.SerializeToString()
    request.senderId = "VISITOR"
    request.sessionId = 0
    struct = request.bodys.add()
    struct.code = 0
    struct.msgId = 1001
    struct.msgBody = msg
    struct.genTime = int(time.time()*1000)
    struct.sequenceId =0
    struct.version = version
    url = "{server}/{version}?id=1001&uid=VISITOR&ver={version}".format(server=server, version=version)
    response = requests.put(url,data=request.SerializeToString())
    if response.status_code==200 : 
        res.ParseFromString(response.content)
        res_1001.ParseFromString(res.bodys[0].msgBody)
        return res_1001
    else:
        print("Server Disconnected ！！!")
        return 0

#进入游戏
def enterGame(res_1001, server,version):
    '''
    参数说明：
    res_1001:login函数返回值\n
    server:https://dtest.gameyici.com(字符串类型)\n
    version:3.1.0(字符串类型)
    '''
    request = GatewayModuleMsg_pb2.GatewayPackageRequest()
    enter = CoreModuleMsg_pb2.EnterGameRequest()
    res = GatewayModuleMsg_pb2.GatewayPackageResponse()
    res_1002 = CoreModuleMsg_pb2.EnterGameResponse()
    request.senderId = res_1001.playerId
    request.sessionId = res_1001.sessionId
    enter.flag = True
    msg = enter.SerializeToString()
    struct = request.bodys.add()
    struct.code = 0
    struct.msgId = 1002
    struct.msgBody = msg
    struct.genTime = int(time.time()*1000)
    struct.sequenceId =0
    struct.version = version
    url = "{server}/{version}?id=1002&uid={playerid}&ver={version}".format(server=server, version=version, playerid=res_1001.playerId)
    response = requests.put(url,data=request.SerializeToString())
    if response.status_code==200 : 
        res.ParseFromString(response.content)
        res_1002.ParseFromString(res.bodys[0].msgBody)
        return res_1002
    else:
        print("Server Disconnected ！！!")
        return 0
        
def protocol_post(requestId, playerid, version, server,session , **kwargs):
    if requestId == "1005":
        completeGuide(server,playerid,version,session,kwargs['guide'])
    elif requestId == "10001":
        taskComplete(server,playerid,version,session,kwargs['scene'],kwargs['task'])
    elif requestId == "10004":
        skipTask(server,playerid,version,session,kwargs['scene'],kwargs['task'])
    elif requestId == "25302":
        obstacleClear(server,playerid,version,session,kwargs['scene'],kwargs['obstacle'])
    elif requestId == "25201":
        getOrder(server,playerid,version,session,kwargs['position'])
    elif requestId == "25401":
        openFarm(server,playerid,version,session,kwargs['farm'])
    elif requestId == "25304":
        buildingUpgrade(server,playerid,version,session,kwargs['scene'],kwargs['building'])
    elif requestId == "24013":
        AccelerateHangUp(server,playerid,version,session,int(kwargs['building']),kwargs['itemid'],int(kwargs['itemcount']))
    elif requestId == "2002":
        useItem(server,playerid,version,session,kwargs['itemid'],int(kwargs['itemcount']))

#加速挂机
def AccelerateHangUp(server,playerid,version,session,creature,item,count):
    request = GatewayModuleMsg_pb2.GatewayPackageRequest()
    body = MagicalCreatureModuleMsg_pb2.AccelerateHangUpRequest()
    res = GatewayModuleMsg_pb2.GatewayPackageResponse()
    request.senderId = playerid
    request.sessionId = session
    body.creatureId = creature
    consum = body.consume
    consum.itemTemplateId=item
    consum.count=count
    msg = body.SerializeToString()
    struct = request.bodys.add()
    struct.code = 0
    struct.msgId = 24013
    struct.msgBody = msg
    struct.genTime = int(time.time()*1000)
    struct.sequenceId = 0
    struct.version = version
    url = "{server}/{version}?id=24013_&uid={playerid}".format(server=server,version=version,playerid=playerid)
    response = requests.put(url,data=request.SerializeToString())
    if response.status_code==200 : 
        res.ParseFromString(response.content)
        if res.bodys[0].code == 0:
            print("useitem:{obstacle} is upgrade!".format(obstacle=item))
            return res
        else:
            print("Error: code={code}".format(code=res.bodys[0].code))
    else:
        print("Server Disconnected ！！!")
        return 0

#使用道具
def useItem(server,playerid,version,session,item,count):
    request = GatewayModuleMsg_pb2.GatewayPackageRequest()
    body = ItemModuleMsg_pb2.UseItemRequest()
    res = GatewayModuleMsg_pb2.GatewayPackageResponse()
    request.senderId = playerid
    request.sessionId = session
    body.itemTemplateId = item
    body.count = count
    body.levelType = 0
    body.useType = 0
    msg = body.SerializeToString()
    struct = request.bodys.add()
    struct.code = 0
    struct.msgId = 2002
    struct.msgBody = msg
    struct.genTime = int(time.time()*1000)
    struct.sequenceId = 0
    struct.version = version
    url = "{server}/{version}?id=2002_&uid={playerid}".format(server=server,version=version,playerid=playerid)
    response = requests.put(url,data=request.SerializeToString())
    if response.status_code==200 : 
        res.ParseFromString(response.content)
        if res.bodys[0].code == 0:
            print("useitem:{obstacle} is upgrade!".format(obstacle=item))
            return res
        else:
            print("Error: code={code}".format(code=res.bodys[0].code))
    else:
        print("Server Disconnected ！！!")
        return 0

#建筑升级
def buildingUpgrade(server,playerid,version,session,scene,build):
    request = GatewayModuleMsg_pb2.GatewayPackageRequest()
    body = SceneModuleMsg_pb2.BuildingLevelUpRequest()
    res = GatewayModuleMsg_pb2.GatewayPackageResponse()
    request.senderId = playerid
    request.sessionId = session
    body.sceneId = scene
    body.plantId = build
    msg = body.SerializeToString()
    struct = request.bodys.add()
    struct.code = 0
    struct.msgId = 25304
    struct.msgBody = msg
    struct.genTime = int(time.time()*1000)
    struct.sequenceId = 0
    struct.version = version
    url = "{server}/{version}?id=25304_&uid={playerid}".format(server=server,version=version,playerid=playerid)
    response = requests.put(url,data=request.SerializeToString())
    if response.status_code==200 : 
        res.ParseFromString(response.content)
        if res.bodys[0].code == 0:
            print("building:{build} is upgrade!".format(build=build))
            return res
        else:
            print("Error: code={code}".format(code=res.bodys[0].code))
    else:
        print("Server Disconnected ！！!")
        return 0

#解锁田地
def openFarm(server,playerid,version,session,farm):
    request = GatewayModuleMsg_pb2.GatewayPackageRequest()
    body = FarmlandModuleMsg_pb2.OpenFarmlandRequest()
    res = GatewayModuleMsg_pb2.GatewayPackageResponse()
    body.plantId = farm
    body.sceneId = "city"
    request.senderId = playerid
    request.sessionId = session
    msg = body.SerializeToString()
    struct = request.bodys.add()
    struct.code = 0
    struct.msgId = 25401
    struct.msgBody = msg
    struct.genTime = int(time.time()*1000)
    struct.sequenceId = 0
    struct.version = version
    url = "{server}/{version}?id=25401_&uid={playerid}".format(server=server,version=version,playerid=playerid)
    response = requests.put(url,data=request.SerializeToString())
    if response.status_code==200 : 
        res.ParseFromString(response.content)
        if res.bodys[0].code == 0:
            print("farm:{guide} is unlock!".format(guide=farm))
        else:
            print("Error: code={code}".format(code=res.bodys[0].code))
    else:
        print("Server Disconnected ！！!")
        return 0

#完成引导
def completeGuide(server,playerid,version,session,guide):
    request = GatewayModuleMsg_pb2.GatewayPackageRequest()
    body = CoreModuleMsg_pb2.GuideCompleteRequest()
    res = GatewayModuleMsg_pb2.GatewayPackageResponse()
    # res_1005 = CoreModuleMsg_pb2.GuideCompleteResponse()
    body.guideId = guide
    request.senderId = playerid
    request.sessionId = session
    msg = body.SerializeToString()
    struct = request.bodys.add()
    struct.code = 0
    struct.msgId = 1005
    struct.msgBody = msg
    struct.genTime = int(time.time()*1000)
    struct.sequenceId = 0
    struct.version = version
    url = "{server}/{version}?id=1005_&uid={playerid}".format(server=server,version=version,playerid=playerid)
    response = requests.put(url,data=request.SerializeToString())
    if response.status_code==200 : 
        res.ParseFromString(response.content)
        # res_1005.ParseFromString(res.bodys[0].msgBody)
        if res.bodys[0].code == 0:
            print("guide:{guide} is complete!".format(guide=guide))
        else:
            print("Error: code={code}".format(code=res.bodys[0].code))
    else:
        print("Server Disconnected ！！!")
        return 0

# 完成任务
def taskComplete(server,playerid,version,session,scene,task):
    request = GatewayModuleMsg_pb2.GatewayPackageRequest()
    res = GatewayModuleMsg_pb2.GatewayPackageResponse()
    body = TaskModuleMsg_pb2.SubmitTaskRequest()
    request.senderId = playerid
    request.sessionId = session
    body.taskId = task
    body.graphId = scene
    msg = body.SerializeToString()
    struct = request.bodys.add()
    struct.code = 0
    struct.msgId = 10001
    struct.msgBody = msg
    struct.genTime = int(time.time()*1000)
    struct.sequenceId = 0
    struct.version = version
    url = "{server}/{version}?id=10001_&uid={playerid}".format(server=server,version=version,playerid=playerid)
    response = requests.put(url,data=request.SerializeToString())
    if response.status_code==200 : 
        res.ParseFromString(response.content)
        # res_1005.ParseFromString(res.bodys[0].msgBody)
        if res.bodys[0].code == 0:
            print("task:{task} is complete!".format(task=task))
        else:
            print("Error: code={code}".format(code=res.bodys[0].code))
    else:
        print("Server Disconnected ！！!")
        return 0

#跳过任务
def skipTask(server,playerid,version,session,scene,task):
    request = GatewayModuleMsg_pb2.GatewayPackageRequest()
    res = GatewayModuleMsg_pb2.GatewayPackageResponse()
    body = TaskModuleMsg_pb2.GMSubmitTaskRequest()
    request.senderId = playerid
    request.sessionId = session
    body.taskId = task
    body.graphId = scene
    msg = body.SerializeToString()
    struct = request.bodys.add()
    struct.code = 0
    struct.msgId = 10004
    struct.msgBody = msg
    struct.genTime = int(time.time()*1000)
    struct.sequenceId = 0
    struct.version = version
    url = "{server}/{version}?id=10004_&uid={playerid}".format(server=server,version=version,playerid=playerid)
    response = requests.put(url,data=request.SerializeToString())
    if response.status_code==200 : 
        res.ParseFromString(response.content)
        # res_1005.ParseFromString(res.bodys[0].msgBody)
        if res.bodys[0].code == 0:
            print("task:{task} is complete!".format(task=task))
        else:
            print("Error: code={code}".format(code=res.bodys[0].code))
    else:
        print("Server Disconnected ！！!")
        return 0

#清除障碍
def obstacleClear(server,playerid,version,session,scene,obstacle):
    request = GatewayModuleMsg_pb2.GatewayPackageRequest()
    body = SceneModuleMsg_pb2.ClearPlantRequest()
    res = GatewayModuleMsg_pb2.GatewayPackageResponse()
    res_25302 = SceneModuleMsg_pb2.ClearPlantResponse()
    request.senderId = playerid
    request.sessionId = session
    body.sceneId = scene
    body.plantId = obstacle
    msg = body.SerializeToString()
    struct = request.bodys.add()
    struct.code = 0
    struct.msgId = 25302
    struct.msgBody = msg
    struct.genTime = int(time.time()*1000)
    struct.sequenceId = 0
    struct.version = version
    url = "{server}/{version}?id=25302_&uid={playerid}".format(server=server,version=version,playerid=playerid)
    response = requests.put(url,data=request.SerializeToString())
    if response.status_code==200 : 
        res.ParseFromString(response.content)
        res_25302.ParseFromString(res.bodys[0].msgBody)
        if res.bodys[0].code == 0:
            print("obstacle:{obstacle} is clear!".format(obstacle=obstacle))
            return res_25302
        else:
            print("Error: code={code}".format(code=res.bodys[0].code))
    else:
        print("Server Disconnected ！！!")
        return 0

#请求订单
def getOrder(server,playerid,version,session,position):
    request = GatewayModuleMsg_pb2.GatewayPackageRequest()
    body = OrderTaskModuleMsg_pb2.AddOrderTaskRequest()
    res = GatewayModuleMsg_pb2.GatewayPackageResponse()
    # res_25201 = SceneModuleMsg_pb2.AddOrderTaskResponse()
    request.senderId = playerid
    request.sessionId = session
    task1 = body.orderTasks.add()
    task1.orderLevel=1
    task1.orderType=2
    task1.position=int(position)
    task1.price=0
    task1.valueTime=0
    item1 = task1.taskItems.add()
    item1.itemTemplateId='5016'
    item1.count=1
    # task2 = body.orderTasks.add()
    # task2.orderLevel=1
    # task2.orderType=2
    # task2.position=2
    # task2.price=0
    # task2.valueTime=0
    # item2 = task2.taskItems.add()
    # item2.itemTemplateId=5016
    # item2.count=2
    # task3 = body.orderTasks.add()
    # task3.orderLevel=1
    # task3.orderType=2
    # task3.position=3
    # task3.price=0
    # task3.valueTime=0
    # item3 = task3.taskItems.add()
    # item3.itemTemplateId=5016
    # item3.count=2
    msg = body.SerializeToString()
    struct = request.bodys.add()
    struct.code = 0
    struct.msgId = 25201
    struct.msgBody = msg
    struct.genTime = int(time.time()*1000)
    struct.sequenceId = 0
    struct.version = version
    url = "{server}/{version}?id=25201_&uid={playerid}".format(server=server,version=version,playerid=playerid)
    response = requests.put(url,data=request.SerializeToString())
    if response.status_code==200 : 
        res.ParseFromString(response.content)
        # res_25201.ParseFromString(res.bodys[0].msgBody)
        if res.bodys[0].code == 0:
            print("order:{order} is setted!".format(order=position))
            return res
        else:
            print("Error: code={code}".format(code=res.bodys[0].code))
    else:
        print("Server Disconnected ！！!")
        return 0




# %%
