#%%

import json

gia = open("D:\\pyprogram\\PyTestTools\\dragon\\tools\\text\\data\\gia.txt","r",encoding="utf-8")
giar = open("D:\\pyprogram\\PyTestTools\\dragon\\tools\\text\\data\\gia_out.txt","w",encoding="utf-8")

custom = {"result","enterid"}

for c in custom:
    giar.write(c+";")
giar.write("\n")

for line in gia:
    line_j = json.loads(line)
    params = line_j["body"]["params"]
    for c in custom:
        try:
            line_out = json.dumps(params[c])
            giar.write(line_out+";")
        except:
            print(line_j["date"])
            giar.write("null"+";")
            pass
    giar.write("\n")

gia.close()
giar.close()
##################################################
# %%  sql导出来的数据
import json

gia = open("gia.txt","r",encoding="utf-8")
giar = open("gia_out.txt","w",encoding="utf-8")

custom = ("method","remain","change")

for c in custom:
    giar.write(c+",")
giar.write("\n")

for line in gia:
    line_j = json.loads(line)
    params = line_j
    for c in custom:
        try:
            line_out = json.dumps(params[c])
            giar.write(line_out+",")
        except:
            print(line_j["ts"])
            giar.write(c+":"+"  "+",")
            pass
    giar.write("\n")

gia.close()
giar.close()
######################################################
# %% 
import json

gia = open("gia.txt","r",encoding="utf-8")
giar = open("gia_out.txt","w",encoding="utf-8")

custom = ("method","timezone")

for c in custom:
    giar.write(c+",")
giar.write("\n")

for line in gia:
    line_j = json.loads(line)
    params = line_j["body"]["device"]
    for c in custom:
        try:
            line_out = json.dumps(params[c])
            giar.write(line_out+",")
        except:
            print(line_j["date"])
            giar.write("null"+",")
            pass
    giar.write("\n")

gia.close()
giar.close()
# %%
