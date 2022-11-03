#%%
import json


gia = ''


giar = ''

custom = ("appver","sysver","devicemodel","devicecountry","syslanguage","timezone")


line_j = json.loads(gia)
params = line_j
for c in custom:
    try:
        line_out = json.dumps(params[c])
        giar+=line_out+","
    except:
        print(line_j["date"])
        giar+="null"+","
        pass
giar+="\n"
print(giar)

# %%
