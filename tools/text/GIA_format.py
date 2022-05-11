#%%

import json

gia = open("gia.txt","r")
giar = open("gia_out.txt","w")

custom = ("farmlandID","cropID","rss","tsl")

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
