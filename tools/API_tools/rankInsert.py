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
server = "38"
activityId = 100005

if server == "38":
    server = "http://dtest.gameyici.com"
elif server == "qa":
    server = "https://dqa.hphorse.net"
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
    log = login(account,server,version="24.1.0")
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
# transcript = {"4l4bzp":799,"5l5bzp":798,"6l6bzp":797,"7l7bzp":590,"8l8bzp":550,"9l9bzp":55,"3l3bzp":50}
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



data_faker["pid"] = "swd29"
data_faker["level"] = 52
data_faker["activityId"] = activityId
data_faker["score"] = 1




data_faker = json.dumps(data_faker)
data_rank.append(data_faker)
RankIns(str(data_rank),server)


