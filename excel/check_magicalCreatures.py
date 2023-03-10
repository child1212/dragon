#%%
import pandas as pd
import json
df = pd.read_excel("E:\\town\\FA\\nfa-config\\excel\\DataFile\\MagicalCreaturesTemplate.xlsx")
#检测id
#品质：等级上限
maxlevel = {1:30,2:40,3:50,4:60}
physicalStrength = {1:1,2:1,3:1,4:2}
upgradeNeedItem = {1:"level*200-100",2:"level*500",3:"level*1000",4:"level*1000"}
productionTime = {1:167,2:119,3:93,4:83}

index_1 = 3


while index_1 < len(df.values):
    phy = physicalStrength.get(df.values[index_1,9])
    m_l = maxlevel.get(df.values[index_1,9])
    cal = upgradeNeedItem.get(df.values[index_1,9])
    timePoint = productionTime.get(df.values[index_1,9])
    #检查id=type*1000+level
    if not df.values[index_1,0] == (df.values[index_1,3])*1000+df.values[index_1,4]:
        print(df.values[index_1,0],'id+type+level')
    #检测quality
    if df.values[index_1,3]//100 != df.values[index_1,9]:
        print(df.values[index_1,0],'quality')
    #检测physicalStrength
    if df.values[index_1,11] != df.values[index_1,4]*phy:
        print(df.values[index_1,0],"physicalStrength")
    if df.values[index_1,12] != 900:
        print(df.values[index_1,0],"physicalStrengthResumeTime")
    if df.values[index_1,31] != 3:
        print(df.values[index_1,0],"production次数")

    #检查品质与等级数量的对应关系
    if df.values[index_1,4]==1:
        for i in range(1,m_l):
            #检测type
            if df.values[index_1,3] != df.values[index_1+i,3]:
                print(df.values[index_1+i,0],'type')
            #检测nextlevel
            if df.values[index_1+i,5] != df.values[index_1+i-1,5]+1:
                if i != m_l-1:
                    print(df.values[index_1+i,0],"nextlevel")
                else:
                    if df.values[index_1+i,5] != 0:
                        print(df.values[index_1+i,0],"nextlevel")
            #检测head
            if df.values[index_1,6] != df.values[index_1+i,6]:
                print(df.values[index_1+i,0],"head")
            #检测icon
            if df.values[index_1,7] != df.values[index_1+i,7]:
                print(df.values[index_1+i,0],"icon")
            #检测model
            if df.values[index_1,8] != df.values[index_1+i,8]:
                print(df.values[index_1+i,0],"model")
            #检测attribute
            if df.values[index_1,10] != df.values[index_1+i,10]:
                print(df.values[index_1+i,0],"attribute")
            #检测升级所需的物品数量
            level = df.values[index_1+i,4]
            if i != m_l-1:
                if json.loads(df.values[index_1+i,14])[0][1] != eval(cal):
                    print(df.values[index_1+i,0],"upgradeNeedItem")
                if json.loads(df.values[index_1+i,14])[0][0] != 1002:
                    print(df.values[index_1+i,0],"upgradeNeedItem")   
            if i == m_l-1:
                if json.loads(df.values[index_1+i,14]) != []:
                    print(df.values[index_1+i,0],"upgradeNeedItem")
            #检测产物一致
            if df.values[index_1,28] != df.values[index_1+i,28]:
                print(df.values[index_1+i,0],"productionID")
            #检测生产时间
            if abs((df.values[index_1+i-1,29]*10000 - df.values[index_1+i,29]*10000)/df.values[index_1,29]-timePoint) > 2:
                if i != m_l-1:
                    print(df.values[index_1+i,0],"productionTime")
            #检测生产数量--没规则做不到
            #if df.values[index_1,30] != 
            



        if index_1+m_l < len(df.values):
            if df.values[index_1,3] == df.values[index_1+m_l,3]:
                print(df.values[index_1+m_l,0],'type')
    





    index_1 += 1

print("除生产数量外，伙伴表检测完毕")



# %%



















