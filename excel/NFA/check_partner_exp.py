#%%

import pandas as pd


mc = pd.read_excel("E:\\FA\\nfa-config\\excel\\DataFile\\MagicalCreaturesTemplate.xlsx")
mc_d = mc.values
quality = {}

for i in range(3, len(mc_d)):
    line = mc_d[i]
    quality[line[3]] = line[9]
    x = eval(line[28])
    if type(x) == list:
        if type(x[1]) != int:
            print(line[0]) 
        if x[0] != 1000:
            print(line[0])
        if len(x) > 2:
            print(line[0])
    else:
        print(line[0])

ww = {1:1,2:10,3:50,4:200}

prs = mc = pd.read_excel("E:\\FA\\nfa-config\\excel\\DataFile\\PartnerRisingStarTemplate.xlsx")
prs_d = prs.values
for i in range(3, len(prs_d)):
    pline = prs_d[i]
    num = ww[quality[pline[2]]]
    if pline[7] != num*(pline[3]-1):
        print(pline[0])




