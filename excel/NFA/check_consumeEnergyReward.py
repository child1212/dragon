#%%
import pandas as pd
import json
import Config


ConsumeEnergyReward =pd.read_excel("{f}\\ConsumeEnergyRewardTemplate.xlsx".format(f=Config.FILE_PATH))

cer = ConsumeEnergyReward.values

#%%
lenth = len(cer)
for i in range(4,lenth):
    a = type(eval(cer[i,5])) == list
    b = eval(cer[i,5])[0] == 6303
    c = type(eval(cer[i,6])) == list
    d = type(eval(cer[i,6])[0]) == list
    e = len(eval(cer[i,6])) == 1
    f = eval(cer[i,6])[0][0] in (1003,1002,15000,1001,30000,11001,42000,60015,16000)


    if a and b and c and d and e and f:
        pass
    else:
        print(i+2,a,b,c,d,e,f)
    
# %%
