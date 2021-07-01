#%%
import requests
import json
import pymysql
import time

def login_gm(host):
    url_login = 'http://10.0.102.197:8084/BI/sys/login'#.format(host=host)

    data_login = {"username":"lienfeng","password":"lienfeng","captcha":""}

    headers_login = {
    "Content-Length":"44",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "http://10.0.102.197:8084",#.format(host=host),
    "Referer": "http://10.0.102.197:8084/BI/login.html",#.format(host=host),
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    return requests.post(url_login, data=data_login, headers=headers_login)

def send_gifts(item_id, item_num, playerid,sessionid , accountid,login_res,host):
    url_sendgift = "http://10.0.102.197:8084/BI/bi/biqatool/option"#.format(host=host)
    
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
    "Origin": "http://10.0.102.197:8084",#.format(host=host),
    "Referer": "http://10.0.102.197:8084/BI/modules/bi/biqatool.html",#.format(host=host),
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    res3 = requests.post(url_sendgift, data =data_sendgift,cookies = login_res.cookies, headers=headers)
    res = res3.text
    res = json.loads(res)
    res = res["msg"]
    return res

def get_playerid(accountid,login_res,host):
    data_checkout = '{"accountId":"qatest102","playerId":"","sessionId":0,"optionIndex":0,"itemId":null,"itemNum":null,"stageId":null,"taskId":null,"newAccount":null,"newPlayerId":null,"buildingId":null,"nickname":null}'
    data_checkout = json.loads(data_checkout)
    data_checkout['accountId'] = accountid
    data_checkout = json.dumps(data_checkout)
    
    url_checkout = 'http://10.0.102.197:8084/BI/bi/biqatool/list'#.format(host=host)

    headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
    "Content-Type": "application/json",
    "Origin": "http://10.0.102.197:8084",#.format(host=host),
    "Referer": "http://10.0.102.197:8084/BI/modules/bi/biqatool.html",#.format(host=host),
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }

    response = requests.post(url_checkout, data =data_checkout,cookies = login_res.cookies, headers=headers)

    res = json.loads(response.text)
    res = json.loads(res['ret'] )
    res = {"playerid":res["playerId"],"sessionid":res["sessionId"]}
    return res

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
    # db = pymysql.connect('localhost','root', '123456', 'Townest')
    # cursor = db.cursor()
    # for i in range(len(item)):
    #     item[i] += 1
    print("account : {acc}".format(acc=account))
    for i in range(len(item)):
        result = send_gifts(item[i], num[i], player,session, account, log_res,server)
        # sql = "select * from items where id = {id};".format(id = item[i])
        # cursor.execute(sql)
        # res = cursor.fetchall()
        # name = res[0][1]
        # n = num[i]
        # res_1 ='{player} - 获取道具  {name}：{num}'.format(player=player,name=name,num=n)
        # res2 = '{result}'.format(result=result)
        # res_3 = '-'*(60-len(res_1)-len(res2)-len(str(name))-len(str(n)))
        # res = res_1+res_3+res2
        # print(res)
    localtime = time.asctime(time.localtime(time.time()))
    print("\n时间\t ：\t",localtime,'\n')
    print("success")
    # db.close()



items = ['1000',
 '1001',
 '1002',
 '1003',
 '2001',
 '2002',
 '2003',
 '2004',
 '2005',
 '2006',
 '2007',
 '2008',
 '2100',
 '5001',
 '5002',
 '5003',
 '5004',
 '5005',
 '5006',
 '5007',
 '5008',
 '5009',
 '5010',
 '5011',
 '5012',
 '5013',
 '5014',
 '5015',
 '5016',
 '5017',
 '5018',
 '5019',
 '5020',
 '5021',
 '5022',
 '3001',
 '3002',
 '3003',
 '3004',
 '3005',
 '3006',
 '3007',
 '3008',
 '3009',
 '3010',
 '3011',
 '3012',
 '3013',
 '3014',
 '3015',
 '3016',
 '3017',
 '3018',
 '3019',
 '3020',
 '3021',
 '3022',
 '3023',
 '3024',
 '3025',
 '3026',
 '3027',
 '3028',
 '3029',
 '3030',
 '3031',
 '3032',
 '3033',
 '3034',
 '3035',
 '3036',
 '3037',
 '3038',
 '3039',
 '3040',
 '3041',
 '3042',
 '3043',
 '3044',
 '3045',
 '3046',
 '3047',
 '3048',
 '3049',
 '3050',
 '3051',
 '3052',
 '3053',
 '3054',
 '3055',
 '3056',
 '4001',
 '4002',
 '4003',
 '4004',
 '4005',
 '4006',
 '4007',
 '4008',
 '4009',
 '4010',
 '4011',
 '4012',
 '4013',
 '4014',
 '4015',
 '4016',
 '4017',
 '4018',
 '4019',
 '4020',
 '4021',
 '4022',
 '4023',
 '4024',
 '4025',
 '4026',
 '4027',
 '4028',
 '4029',
 '4030',
 '4031',
 '4032',
 '4033',
 '4034',
 '4035',
 '4036',
 '4037',
 '4038',
 '4039',
 '4040',
 '4041',
 '4042',
 '4043',
 '4044',
 '4045',
 '4046',
 '4047',
 '4048',
 '4049',
 '4050',
 '4051',
 '4052',
 '4053',
 '4054',
 '4055',
 '4056',
 '4057',
 '4058',
 '4059',
 '4060',
 '4061',
 '4062',
 '4063',
 '4064',
 '4065',
 '4066',
 '4067',
 '6001',
 '6002',
 '6003',
 '6004',
 '6005',
 '6006',
 '6007',
 '6008',
 '6009',
 '6010',
 '6011',
 '6012',
 '6013',
 '6014',
 '7001',
 '7002',
 '7003',
 '7004',
 '7005',
 '8001',
 '8002',
 '8003',
 '8004',
 '8005',
 '8006',
 '8007',
 '8008',
 '9001',
 '9002',
 '9003',
 '10001',
 '10002',
 '10003',
 '10004',
 '10005',
 '11001',
 '13001',
 '14001',
 '14002',
 '14003',
 '14004',
 '14011',
 '14012',
 '14013',
 '14014',
 '14021',
 '14022',
 '14023',
 '14024',
 '14031',
 '14032',
 '14033',
 '14034',
 '14041',
 '14042',
 '14043',
 '14044',
 '14051',
 '14052',
 '14053',
 '14054',
 '14061',
 '14062',
 '14063',
 '14064',
 '14071',
 '14072',
 '14073',
 '14074',
 '14081',
 '14082',
 '14083',
 '14084',
 '14091',
 '14092',
 '14093',
 '14094',
 '14101',
 '14102',
 '14103',
 '14104',
 '14111',
 '14112',
 '14113',
 '14114',
 '14121',
 '14122',
 '14123',
 '14124',
 '14131',
 '14132',
 '14133',
 '14134',
 '14141',
 '14142',
 '14143',
 '14144',
 '14151',
 '14152',
 '14153',
 '14154',
 '14161',
 '14162',
 '14163',
 '14164',
 '14171',
 '14172',
 '14173',
 '14174',
 '14181',
 '14182',
 '14183',
 '14184',
 '14191',
 '14192',
 '14193',
 '14194',
 '14201',
 '14202',
 '14203',
 '14204',
 '14211',
 '14212',
 '14213',
 '14214']
items = range(1001, 1004)
account = 1004
num = [-1000]*len(items)
server = ''
senditems(account, items, num, server)
#%%
