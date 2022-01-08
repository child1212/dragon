#%%
import json

txt = open("point.txt","r")
dic = dict()

for line in txt:
    l = line.replace("\n", "")
    dic[l] = l

j = json.dumps(dic)
txt.close()
print('a:',j)
