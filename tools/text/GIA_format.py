#%%

import json

gia = open("gia.txt","r",encoding="utf-8")
giar = open("gia_out.txt","w",encoding="utf-8")

custom = ("playerid","errorCode")

for line in gia:
    line_j = json.loads(line)
    params = line_j["body"]["params"]
    for c in custom:
        try:
            line_out = json.dumps(params[c])
            giar.write(c+":"+line_out+",")
        except:
            print(line_j["date"])
            giar.write(c+":"+"  "+",")
            pass
    giar.write("\n")

gia.close()
giar.close()
# %%
import json

gia = open("gia.txt","r",encoding="utf-8")
giar = open("gia_out.txt","w",encoding="utf-8")

custom = ("playerid","errorCode")

for line in gia:
    line_j = json.loads(line)
    params = line_j
    for c in custom:
        try:
            line_out = json.dumps(params[c])
            giar.write(c+":"+line_out+",")
        except:
            print(line_j["ts"])
            giar.write(c+":"+"  "+",")
            pass
    giar.write("\n")

gia.close()
giar.close()
# %%
