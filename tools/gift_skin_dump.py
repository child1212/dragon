#%%
import pandas as pd

a = [[["470"],[[27525,1],[27513,1]]],[["471"],[[27689,1],[27686,1]]],[["472"],[[27521,1],[27689,1]]],[["334"],[[143201,1],[1003,1600]]],[["335"],[[143701,1],[1003,1600]]],[["336"],[[141501,1],[1003,1600]]]]






skintemp = pd.read_excel("E:\\town\\dragon\\dragon-config\\excel\\DataFile\\SkinTemplate.xlsx")
magic = pd.read_excel("E:\\town\\dragon\\dragon-config\\excel\\DataFile\\MagicalCreaturesTemplate.xlsx")

skins = {}
creatures ={1003:"体力"}

for line in skintemp.values:
    skins[line[0]] = line[1]
for line in magic.values:
    creatures[line[0]] = line[3]

for x in range(6):
    if x < 3:
        for j in a[x][1]:
            j[0] = skins[j[0]]
    else:
        for j in a[x][1]:
            j[0] = creatures[j[0]]
a            