#########################################################
#%%
#初始化
from time import sleep
import sys
sys.path.append('D:\\pyprogram\\PyTestTools\\dragon\\function')
import requests
import json
import random
from xieyi import *
server = "ntest"
activityId = 9001

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
def RankIns(data,host="https://dqa.hphorse.net"):
    url_banding = "{host}/BI/open/disMatch".format(host=host)
    headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "Content-Type": "application/json",
    "Origin": "{host}".format(host=host),
    "Referer": "{host}/BI/open/disMatch".format(host=host)
    }

    res3 = requests.post(url_banding, data, headers=headers)
    res = res3.text
    # res = json.loads(res)
    # res = res["msg"]
    print(res)
data = {}

########################################################
#%%
#插入机器人
for i in range(100):
    account = "act{i}".format(i=i)
    log = login(account,server,version="2.1.0")
    data_rank = []
    data_faker = '{"pid":"","level":0,"activityId":0,"score":0}'
    data_faker = json.loads(data_faker)
    pid = log.playerId
    level = random.choice(range(12,40))
    score = i+100 #random.choice(range(50,100))
    data_faker["pid"] = pid
    data_faker["level"] = 16
    data_faker["activityId"] = activityId
    data_faker["score"] = score
    data_faker = json.dumps(data_faker)
    data_rank.append(data_faker)
    RankIns(str(data_rank),server)
    # time.sleep(3)
    data[account] = (level,score)


#######################################################
# %%
#插入1890-1896
transcript = {"li2001":799,"li2002":798,"li2003":797,"li2004":290,"li2005":250,"li2006":55,"li2000":99}
transcript = {"li0001":799,"li0002":798,"li0003":797,"li0004":290,"li0005":250,"li0006":55,"li0007":99}
transcript = {"swd29":2,"swd28":100,"swd27":148,"swd26":180,"swd25":190,"swd24":1,"swd23":700,"swd22":1178,"swd21":1179,"swd20":1180}#pid:分数
for key in transcript:
    data_rank = []
    data_faker = '{"pid":"","level":0,"activityId":0,"score":0}'
    data_faker = json.loads(data_faker)
    level = random.choice(range(12,40))


    data_faker["pid"] = key
    data_faker["level"] = 14
    data_faker["activityId"] = activityId
    data_faker["score"] = transcript[key]


    data_faker = json.dumps(data_faker)
    data_rank.append(data_faker)
    RankIns(str(data_rank),server)


########################################################
# %%
#插入单个玩家
data_rank = []
data_faker = '{"pid":"","level":0,"activityId":0,"score":0}'
data_faker = json.loads(data_faker)
level = random.choice(range(12,40))



data_faker["pid"] = "5l5bzp"
data_faker["level"] = 52
data_faker["activityId"] = 9003
data_faker["score"] = 95




data_faker = json.dumps(data_faker)
data_rank.append(data_faker)
RankIns(str(data_rank),server)


