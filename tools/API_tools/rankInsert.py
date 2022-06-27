
#%%
from time import sleep
import requests
import json
import random

# data_rank = []
# for i in range(100):
#     data_rank = []
#     data_faker = '{"pid":"faker1","level":12,"activityId":1002,"score":10}'
#     data_faker = json.loads(data_faker)
#     data_faker["pid"] = "faker{i}".format(i=i+1)
#     data_faker["level"] = random.choice(range(12,50))
#     data_faker["activityId"] = 1002
#     data_faker["score"] = random.choice(range(1000))
#     data_faker = json.dumps(data_faker)
#     data_rank.append(data_faker)
#     RankIns(str(data_rank))

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
#%%
for i in range(200):
    data_rank = []
    data_faker = '{"pid":"","level":0,"activityId":0,"score":0}'
    data_faker = json.loads(data_faker)
    pid = "faker{i}".format(i=i+1)
    level = random.choice(range(12,40))
    score = i+5 #random.choice(range(50,100))
    data_faker["pid"] = pid
    data_faker["level"] = level
    data_faker["activityId"] = 103
    data_faker["score"] = score
    data_faker = json.dumps(data_faker)
    data_rank.append(data_faker)
    RankIns(str(data_rank))
    # time.sleep(3)
    data["faker{i}".format(i=i+1)] = (level,score)

# RankIns(str(data_rank))
# %%
data_rank = []
data_faker = '{"pid":"","level":0,"activityId":0,"score":0}'
data_faker = json.loads(data_faker)
level = random.choice(range(12,40))



data_faker["pid"] = "dtdzed"
data_faker["level"] = level
data_faker["activityId"] = 103
data_faker["score"] = 250



data_faker = json.dumps(data_faker)
data_rank.append(data_faker)
RankIns(str(data_rank))
# time.sleep(3)
data["faker{i}".format(i=i+1)] = (level,score)