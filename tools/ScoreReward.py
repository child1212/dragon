from time import sleep
import sys
sys.path.append('D:\\pyprogram\\PyTestTools\\dragon\\function')
import requests
import json
import random
from xieyi import *

print("请提前检查奖励积分配置！！！！！")
print("请提前检查奖励积分配置！！！！！")
print("请提前检查奖励积分配置！！！！！")

server = "act"
activityId = int(input("activityid:"))
playerid = input("playerid:")
level = int(input("level:"))

if server == "38":
    server = "http://dtest.gameyici.com"
elif server == "qa":
    server = "https://dqa.hphorse.net"
elif server == "act":
    server = "http://dact.gameyici.com"
#构造修改玩家数据的函数
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
# data = {}




#创建奖品名称映射
mine = {}
table_item = open("D:\\pyprogram\\PyTestTools\\dragon\\tools\\ItemTemplate.csv","r",encoding="utf-8-sig")
item = {}
for line in table_item:
    line_l = line.split(",")
    item[str(line_l[0])] = line_l[1]
table_item.close()

#打开配置文件
sr = open("D:\\pyprogram\\PyTestTools\\dragon\\tools\\ScoreReward.txt","r")
for line in sr:
    line = line.replace("\n","")
#llll是配置，格式[分数，[[奖励1,数量],[奖励2,数量]]]
    llll = line.split("\t")

#修改玩家积分
    data_rank = []
    data_faker = '{"pid":"","level":0,"activityId":0,"score":0}'
    data_faker = json.loads(data_faker)
    data_faker["pid"] = playerid
    data_faker["level"] = level
    data_faker["activityId"] = activityId
    data_faker["score"] = int(llll[0])-1
    data_faker = json.dumps(data_faker)
    data_rank.append(data_faker)
    RankIns(str(data_rank),server)




#统计奖励数量并打印
    for reward in eval(llll[1]):
        if reward[0] in mine:
            mine[reward[0]] += reward[1]
        else:
            mine[reward[0]] = reward[1]
        print("{name}:{num}".format(name=item[str(reward[0])],num=mine[reward[0]]))
    # for i in mine:
    #     print("{name}:{num}".format(name=item[str(i)],num=mine[i]))
    input("contune?")
    print("============================\n")
sr.close()

