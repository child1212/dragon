#%%
import pandas as pd
import json
df = pd.read_excel("E:\\FA\\nfa-config\\excel\\DataFile\\MagicalCreaturesTemplate.xlsx")
#检测id
#品质：等级上限
maxlevel = {1:15,2:15,3:15,4:15}
physicalStrength = {1:1,2:2,3:3,4:5}
upgradeNeedItem = {1:"level*200-100",2:"level*500",3:"level*1000",4:"level*1000"}
productionTime = {1:0,2:0,3:0,4:0}

index_1 = 3
title = {}
for i in range(len(df.values[0])):
    title[df.values[0][i]] = i


while index_1 < len(df.values):
    phy = physicalStrength.get(df.values[index_1,9])
    m_l = maxlevel.get(df.values[index_1,9])
    cal = upgradeNeedItem.get(df.values[index_1,9])
    timePoint = productionTime.get(df.values[index_1,9])
    #检查id=type*1000+level
    if not df.values[index_1,0] == (df.values[index_1,title.get("type")])*1000+df.values[index_1,title.get("level")]:
        print(df.values[index_1,0],'id+type+level')
    #检测quality
    if df.values[index_1,0]//1000 != 111:
        if df.values[index_1,title.get("type")]//100 != df.values[index_1,title.get("quality")]:
            print(df.values[index_1,0],'quality')
    elif df.values[index_1,0]//1000 == 111:
        if df.values[index_1,title.get("quality")] != 2:
            print(df.values[index_1,0],'quality')
    #检测physicalStrength
    if df.values[index_1,title.get("physicalStrength")] != df.values[index_1,title.get("level")]*phy:
        print(df.values[index_1,0],"physicalStrength")
    #检测童话之力回复时间
    if df.values[index_1,title.get("physicalStrengthResumeTime")] != 900:
        print(df.values[index_1,0],"physicalStrengthResumeTime")
    #检测伙伴生产次数
    if json.loads(df.values[index_1,title.get("productivity")])[3] != 3:
        print(df.values[index_1,0],"production次数")

    #检查品质与等级数量的对应关系
    if df.values[index_1,title.get("level")]==1:
        for i in range(1,m_l):
            #检测type
            if df.values[index_1,title.get("type")] != df.values[index_1+i,title.get("type")]:
                print(df.values[index_1+i,0],'type')
            #检测nextlevel
            if df.values[index_1+i,title.get("nextLevel")] != df.values[index_1+i-1,title.get("nextLevel")]+1:
                if i != m_l-1:
                    print(df.values[index_1+i,0],"nextlevel")
                else:
                    if df.values[index_1+i,title.get("nextLevel")] != 0:
                        print(df.values[index_1+i,0],"nextlevel")
            #检测head
            if df.values[index_1,title.get("head")] != df.values[index_1+i,title.get("head")]:
                print(df.values[index_1+i,0],"head")
            #检测icon
            if df.values[index_1,title.get("icon")] != df.values[index_1+i,title.get("icon")]:
                print(df.values[index_1+i,0],"icon")
            #检测model
            if df.values[index_1,title.get("model")] != df.values[index_1+i,title.get("model")]:
                print(df.values[index_1+i,0],"model")
            #检测attribute
            if df.values[index_1,title.get("attribute")] != df.values[index_1+i,title.get("attribute")]:
                print(df.values[index_1+i,0],"attribute")
            #检测升级所需的物品数量
            # level = df.values[index_1+i,title.get("level")]
            # if i != m_l-1:
            #     if json.loads(df.values[index_1+i,title.get("upgradeNeedItem")])[0][1] != eval(cal):
            #         print(df.values[index_1+i,0],"upgradeNeedItem")
            #     if json.loads(df.values[index_1+i,title.get("upgradeNeedItem")])[0][0] != 1002:
            #         print(df.values[index_1+i,0],"upgradeNeedItem")   
            # if i == m_l-1:
            #     if json.loads(df.values[index_1+i,title.get("upgradeNeedItem")]) != []:
            #         print(df.values[index_1+i,0],"upgradeNeedItem")
            #检测产物一致
            if json.loads(df.values[index_1,title.get("productivity")])[0] != json.loads(df.values[index_1+i,title.get("productivity")])[0]:
                print(df.values[index_1+i,0],"productionID")
            #检测生产时间
            # if abs((json.loads(df.values[index_1+i-1,title.get("productivity")])[1]*10000 - json.loads(df.values[index_1+i,title.get("productivity")])[1]*10000)/json.loads(df.values[index_1,title.get("productivity")])[1]-timePoint) > 2:
            #     if i != m_l-1:
            #         if df.values[index_1,title.get("type")] != 304:
            #             print(df.values[index_1+i,0],"productionTime")
            # if not 0.45 <= ((json.loads(df.values[index_1+i-1,title.get("productivity")])[1] - json.loads(df.values[index_1+i,title.get("productivity")])[1])/json.loads(df.values[index_1,title.get("productivity")])[1])*m_l <= 0.5 :
            # if ((json.loads(df.values[index_1+i-1,title.get("productivity")])[1] - json.loads(df.values[index_1+i,title.get("productivity")])[1])/json.loads(df.values[index_1,title.get("productivity")])[1])*m_l != 0 :

            #     if i != m_l-1:
            #         if df.values[index_1,title.get("type")] != 304:
            #             print(df.values[index_1+i,0],"productionTime",((json.loads(df.values[index_1+i-1,title.get("productivity")])[1] - json.loads(df.values[index_1+i,title.get("productivity")])[1])/json.loads(df.values[index_1,title.get("productivity")])[1])*m_l)
            #检测生产数量--没规则做不到
            #if df.values[index_1,30] != 
            



        if index_1+m_l < len(df.values):
            if df.values[index_1,3] == df.values[index_1+m_l,3]:
                print(df.values[index_1+m_l,0],'type')
    





    index_1 += 1
print("除生产数量外，伙伴表检测完毕")
print("需要测试各伙伴1级的表现")



# %%



















