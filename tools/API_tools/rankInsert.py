#########################################################
#%%
#初始化
from time import sleep

import os
pack_pos = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
import sys
sys.path.append('{pack_pos}\\function'.format(pack_pos=pack_pos))
import requests
import json
import random
from xieyi import *
server = "38"
activityId = 100005
version="44.1.0"



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
    account = "try{i}".format(i=i)
    log = login(account,server,version)
    data_rank = []
    data_faker = '{"pid":"","level":0,"activityId":0,"score":0}'
    data_faker = json.loads(data_faker)
    pid = log.playerId
    level = random.choice(range(12,40))
    score = i+200 #random.choice(range(50,100))
    data_faker["pid"] = pid
    data_faker["level"] = 17
    data_faker["activityId"] = activityId
    data_faker["score"] = score
    data_faker = json.dumps(data_faker)
    data_rank.append(data_faker)
    RankIns(str(data_rank),server)
    time.sleep(3)
    data[account] = (level,score)


#######################################################
# %%
#插入1890-1896
transcript = {"swd29":2,"swd28":200,"swd27":248,"swd26":280,"swd25":290,"swd24":1,"swd23":700,"swd22":1178,"swd21":1179,"swd20":1180}#pid:分数
# transcript = {"swd50":500+300,"swd51":499+300,"swd52":498+300,"swd53":497+300,"swd54":100,"swd55":290,"swd56":280,"swd57":240}#pid:分数
# transcript = {"onl799":5000,"onl798":4999,"onl797":4998,"onl796":4997,"onl795":100,"wb3qqk":290}#pid:分数

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



data_faker["pid"] = "max014"
data_faker["level"] = 59
data_faker["activityId"] = activityId
data_faker["score"] = 130




data_faker = json.dumps(data_faker)
data_rank.append(data_faker)
RankIns(str(data_rank),server)


