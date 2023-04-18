#%%
import json

data = open("D:\\pyprogram\\PyTestTools\\dragon\\tools\\text\\data\\count.txt","r",encoding="utf-8")
datar = open("D:\\pyprogram\\PyTestTools\\dragon\\tools\\text\\data\\count_result.txt","w",encoding="utf-8")

d = {}

for line in data:
    line = line.replace('\n','')
    if d.get(line):
        d[line] += 1
    else:
        d[line] = 1

data.close()
for i in d:
    datar.write("{i}:{num}\n".format(i=i,num=d[i]))

datar.close()

