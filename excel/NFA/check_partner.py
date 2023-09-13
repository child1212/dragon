#%%
import pandas as pd
import json

bubble_file = pd.read_excel("E:\\FA\\nfa-config\\excel\\DataFile\\PartnerbubbleTemplate.xlsx")
risingstar_file = pd.read_excel("E:\\FA\\nfa-config\\excel\\DataFile\\PartnerRisingStarTemplate.xlsx")
mc = pd.read_excel("E:\\FA\\nfa-config\\excel\\DataFile\\MagicalCreaturesTemplate.xlsx")

mc_values = mc.values
bubble_values = bubble_file.values
risingstar_values = risingstar_file.values

id_set_mc =set()
id_set_bubble = set()
id_set_risingstar = set()

for i in range(3,len(bubble_values)):
    id_set_mc.add(mc_values[i][3])
for i in range(3,len(bubble_values)):
    id_set_bubble.add(bubble_values[i][0])
for i in range(3,len(risingstar_values)):
    id_set_risingstar.add(risingstar_values[i][2])

x = id_set_mc - id_set_risingstar
y = id_set_risingstar - id_set_bubble
print("升星少了：",x)
print("气泡少了：",y)
# %%
