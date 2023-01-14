#%%
import json
import pyperclip

txt = open("point.txt","r")
dic = dict()

for line in txt:
    l = line.replace("\n", "")
    dic[l] = l

dic["level"] = ''
dic["platform"] = ''
dic["playerid"] = ''
dic["deviceId"] = ''
dic["ts"] = ''
dic["version"] = ''
# dic["server"] = ''
# dic["ads_group_id"] = ''
dic["rss"] = ''
dic["tsl"] = ''
j = json.dumps(dic)
txt.close()
pyperclip.copy(j)
# %%
