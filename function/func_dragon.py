import requests
import json
import time


def banding(accountid,playerid,host,login_res):
    url_banding = "{host}/BI/bi/biqatool/option".format(host=host)
    
    data_banding = '{"accountId":"gm","playerId":"100","sessionId":0,"optionIndex":9,"itemId":null,"itemNum":null,"stageId":null,"taskId":null,"newAccount":"673B07E9-B388-4CA3-82BE-EF1F88A66CD2","newPlayerId":"e8kqb0","buildingId":null,"nickname":null}'
    data_banding = json.loads(data_banding)
    data_banding["newAccount"] = accountid
    data_banding["newPlayerId"] = playerid
    data_banding = json.dumps(data_banding)

    headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "Content-Type": "application/json",
    "Origin": "{host}".format(host=host),
    "Referer": "{host}/BI/modules/bi/biqatool.html".format(host=host)
    }

    res3 = requests.post(url_banding, data =data_banding,cookies = login_res.cookies, headers=headers)
    res = res3.text
    res = json.loads(res)
    res = res["msg"]
    return res


#调关和任务
def riselevel(account, level, task, server):
    '''
    account:str
    level:int -- 目标关卡位置
    task:int -- 需要完成的任务数量
    server:<dev:"tlogin", qa:"qausa"> 
    '''
    log_res = login_gm(server)                      #登录GM平台

    try:
        info = get_playerid(account, log_res,server)    #获取playerId
        player = info['playerid']
        session = info['sessionid']
        print('调整等级: [{l}]  / 调整任务:[{t}]'.format(l=str(level),t=str(task)))
        result = level_task(player,session,account,str(level-1),str(task),log_res,server)
        print('{acc} : {p}-----------------------------------------------{result}\n '.format(acc=account,p=player,result=result))
    except:
        print('调整任务等级  {acc}  ---------------------------------------账号未创建'.format(acc=account))



#发道具
def senditems(account, item, num, server):
    '''
    account:str
    item:list[int]
    num:list[int]
    server:<dev:"tlogin", qa:"qausa"> 
    '''
    log_res = login_gm(server)                      #登录GM平台
    info = get_playerid(account, log_res,server)    #获取playerId
    player = info['playerid']
    session = info['sessionid']
    db = pymysql.connect('localhost','root', '123456', 'Townest')
    cursor = db.cursor()
    # for i in range(len(item)):
    #     item[i] += 1
    print("account : {acc}".format(acc=account))
    for i in range(len(item)):
        result = send_gift(item[i], num[i], player,session, account, log_res,server)
        sql = "select * from items where id = {id};".format(id = item[i])
        cursor.execute(sql)
        res = cursor.fetchall()
        name = res[0][1]
        n = num[i]
        res_1 ='{player} - 获取道具  {name}：{num}'.format(player=player,name=name,num=n)
        res2 = '{result}'.format(result=result)
        res_3 = '-'*(60-len(res_1)-len(res2)-len(str(name))-len(str(n)))
        res = res_1+res_3+res2
        print(res)
    localtime = time.asctime(time.localtime(time.time()))
    print("\n时间\t ：\t",localtime,'\n')
    db.close()


#获取playerid
def get_playerid(accountid,login_res,host):
    data_checkout = '{"accountId":"qatest102","playerId":"","sessionId":0,"optionIndex":0,"itemId":null,"itemNum":null,"stageId":null,"taskId":null,"newAccount":null,"newPlayerId":null,"buildingId":null,"nickname":null}'
    data_checkout = json.loads(data_checkout)
    data_checkout['accountId'] = accountid
    data_checkout = json.dumps(data_checkout)
    
    url_checkout = '{host}/BI/bi/biqatool/list'.format(host=host)

    headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
    "Content-Type": "application/json",
    "Origin": "{host}".format(host=host),
    "Referer": "{host}/BI/modules/bi/biqatool.html".format(host=host),
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }

    response = requests.post(url_checkout, data =data_checkout,cookies = login_res.cookies, headers=headers)

    res = json.loads(response.text)
    res = json.loads(res['ret'] )
    res = {"playerid":res["playerId"],"sessionid":res["sessionId"]}
    return res
#获取accountid
def get_accountid(playerid,login_res,host):
    data_checkout = '{"accountId":"","playerId":"","sessionId":0,"optionIndex":0,"itemId":null,"itemNum":null,"stageId":null,"taskId":null,"newAccount":null,"newPlayerId":null,"buildingId":null,"nickname":null}'
    data_checkout = json.loads(data_checkout)
    data_checkout['playerId'] = playerid
    data_checkout = json.dumps(data_checkout)
    
    url_checkout = '{host}/BI/bi/biqatool/list'.format(host=host)

    headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
    "Content-Type": "application/json",
    "Origin": "{host}".format(host=host),
    "Referer": "{host}/BI/modules/bi/biqatool.html".format(host=host),
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }

    response = requests.post(url_checkout, data =data_checkout,cookies = login_res.cookies, headers=headers)

    res = json.loads(response.text)
    res = json.loads(res['ret'] )
    res = {"accountid":res["accountId"],"sessionid":res["sessionId"]}
    return res
#登录gm工具
def login_gm(host):
    url_login = '{host}/BI/sys/login'.format(host=host)

    data_login = {"username":"lienfeng","password":"lienfeng","captcha":""}

    headers_login = {
    "Content-Length":"44",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "{host}".format(host=host),
    "Referer": "{host}/BI/login.html".format(host=host),
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    return requests.post(url_login, data=data_login, headers=headers_login)

#获取道具列表（list）
def get_itemlist(playerid,sessionid,accountid,login_res,host):
    url_itemlist = "{host}/BI/bi/biqatool/queryitem".format(host=host)
    
    data_itemlist = '{"accountId":"qatest103","playerId":"9t3vry","sessionId":0,"optionIndex":1,"itemId":null,"itemNum":null,"stageId":null,"taskId":null,"newAccount":null,"newPlayerId":null,"buildingId":null,"nickname":null}'
    data_itemlist = json.loads(data_itemlist)
    data_itemlist["accountId"] = accountid
    data_itemlist["playerId"] = playerid
    data_itemlist["sessionId"] = sessionid
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

    res_item = requests.post(url_itemlist, data =data_itemlist,cookies = login_res.cookies, headers=headers)
    res_list = res_item.text
    res_list = json.loads(res_list)
    return res_list

#发道具
def send_gift(item_id, item_num, playerid,sessionid , accountid,login_res,host):
    url_sendgift = "{host}/BI/bi/biqatool/option".format(host=host)
    
    data_sendgift = '{"accountId":"qatest102","playerId":"ogvct8","sessionId":0,"optionIndex":1,"itemId":"","itemNum":"","stageId":null,"taskId":null,"newAccount":null,"newPlayerId":null,"buildingId":null,"nickname":null}'
    data_sendgift = json.loads(data_sendgift)
    data_sendgift["accountId"] = accountid
    data_sendgift["playerId"] = playerid
    data_sendgift["sessionId"] = sessionid
    data_sendgift["itemId"] = str(item_id)
    data_sendgift["itemNum"] = str(item_num)
    data_sendgift = json.dumps(data_sendgift)

    headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
    "Content-Type": "application/json",
    "Origin": "{host}".format(host=host),
    "Referer": "{host}/BI/modules/bi/biqatool.html".format(host=host),
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    
    
    
    res3 = requests.post(url_sendgift, data =data_sendgift,cookies = login_res.cookies, headers=headers)
    res = res3.text
    res = json.loads(res)
    res = res["msg"]
    return res

#账号解绑
def untie(playerid,sessionid,accountid,login_res,host):
    url_untie = "{host}/BI/bi/biqatool/option".format(host=host)

    data_untie = '{"accountId":"qa_12.1_0","playerId":"9cnkmo","sessionId":0,"optionIndex":0,"itemId":null,"itemNum":null,"stageId":null,"taskId":null,"newAccount":null,"newPlayerId":null,"buildingId":null,"nickname":null}'
    data_untie = json.loads(data_untie)
    data_untie["accountId"] = accountid
    data_untie["playerId"] = playerid
    data_untie["sessionId"] = sessionid
    data_untie = json.dumps(data_untie)

    headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
    "Content-Type": "application/json",
    "Origin": "{host}".format(host=host),
    "Referer": "{host}/BI/modules/bi/biqatool.html".format(host=host),
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }

    res3 = requests.post(url_untie, data =data_untie,cookies = login_res.cookies, headers=headers)
    res = res3.text
    res = json.loads(res)
    res = res["msg"]
    return res

#修改关卡和任务
def level_task(playerid,sessionid,accountid,levelid,taskid,login_res,host):
    url_level = "{host}/BI/bi/biqatool/option".format(host=host)

    data_lt = '{"accountId":"dev_14.1_1","playerId":"7f1nau","sessionId":0,"optionIndex":2,"itemId":null,"itemNum":null,"stageId":"21","taskId":"1","newAccount":null,"newPlayerId":null,"buildingId":null,"nickname":null}'
    data_lt = json.loads(data_lt)
    data_lt["accountId"] = accountid
    data_lt["playerId"] = playerid
    data_lt["sessionId"] = sessionid
    data_lt["stageId"] = levelid
    data_lt["taskId"] = taskid

    data_lt = json.dumps(data_lt)

    headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
    "Content-Type": "application/json",
    "Origin": "{host}".format(host=host),
    "Referer": "{host}/BI/modules/bi/biqatool.html".format(host=host),
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }

    res3 = requests.post(url_level, data =data_lt,cookies = login_res.cookies, headers=headers)
    res = res3.text
    res = json.loads(res)
    res = res["msg"]
    return res


def clear_item(playerid,login_res,host):
    url_itemlist = "{host}/BI/bi/bieditplayerdata/update".format(host=host)
    data_itemlist = '{"rowKey":"Pjsjk95@{jsjk95}-Item","rowValue":"{\\n\\t\\"items\\": []}","note":null,"serverId":null}'
    data_itemlist = json.loads(data_itemlist)
    data_itemlist["rowKey"] = 'Pplayerid@{playerid}-Item'.replace('playerid',playerid)
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

    res_item = requests.post(url_itemlist, data =data_itemlist,cookies = login_res.cookies, headers=headers)
    res_list = res_item.text
    res_list = json.loads(res_list)
    return res_list

def get_player_info(accountid,playerid,host,login_res):
    url_get_info = '{host}/BI/bi/bieditplayerdata/list?_search=false&nd={ts}&limit=100&page=1&sidx=&order=asc&serverId=&pid={playerid}&aId={account}&_={ts}'.format(ts=int(time.time()*1000),host=host,playerid=playerid,account=accountid)


    headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "Content-Type": "application/json",
    "Origin": "{host}".format(host=host),
    "Referer": "{host}/BI/modules/bi/bieditplayerdata.html".format(host=host)
    }

    res3 = requests.get(url_get_info,cookies = login_res.cookies, headers=headers)
    res = res3.text
    res = json.loads(res)
    return res


def change_Properties(info,playerid,login_res,host,params):
    key = "P{playerid}@{{{playerid}}}-Properties".format(playerid=playerid)
    value = info[key]
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







