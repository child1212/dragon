#%%
import pandas as pd
import json
import Config

goldPassLevel = pd.read_excel("{f}\\GoldPassLevelTemplate.xlsx".format(f=Config.FILE_PATH))

gpl = goldPassLevel.values

ids = set()

lenth = len(gpl)
for i in range(4,lenth):
    #检测id不重复
    if gpl[i,0] in ids:
        print("id重复:",gpl[i,0])
    ids.add(gpl[i,0])
    if i > 30:
        #比对等级
        if gpl[i,1] != gpl[i-27,1]:
            print(gpl[i,0],":",gpl[0,1]) 
        
        #对比活动id
        if gpl[i,2] != gpl[i-27,2]+1:
            print(gpl[i,0],":",gpl[0,2])
        
        #比对下一级需要的经验
        if gpl[i,3] != gpl[i-27,3]:
            print(gpl[i,0],":",gpl[0,3])
        
        #比对普通奖励类型
        if gpl[i,5] != gpl[i-27,5]:
            print(gpl[i,0],":",gpl[0,5])
        
        #对比普通奖励
        if gpl[i,6] != gpl[i-27,6]:
            print(gpl[i,0],":",gpl[0,6])

        #比对VIP奖励类型
        if gpl[i,7] != gpl[i-27,7]:
            print(gpl[i,0],":",gpl[0,7])
        
        #比对购买等级消耗钻石数
        if gpl[i,9] != gpl[i-27,9]:
            print(gpl[i,0],":",gpl[0,9])
        
        #比对是否为特殊奖励
        if gpl[i,12] != gpl[i-27,12]:
            print(gpl[i,0],":",gpl[0,12])
        
        #比对是否为阶段奖励
        if gpl[i,13] != gpl[i-27,13]:
            print(gpl[i,0],":",gpl[0,13])

        
        #检测本期活动配置与上期活动配置区别
        if i > lenth-29:
            # if i == lenth-27:
            #     print("奖励帽子图标：",gpl[i,4])
            #     hat_icon = gpl[i,4]
            #     print("奖励帽子id:",gpl[i,8])
            #     hat_id = gpl[i,8]
            #     print("奖励帽子名称:",gpl[i,10])
            #     hat_name = gpl[i,10]
            #     print("奖励帽子描述:",gpl[i,11])
            #     hat_des = gpl[i,11]
            if i == lenth-13:
                #比对奖励icon
                if gpl[i,4] == gpl[i-27,4]:
                    if str(gpl[i,4]) != "nan":
                        print(gpl[i,0],":",gpl[0,4],"--",gpl[i,4],"奖励一样了")

                #比对VIP奖励
                if gpl[i,8] == gpl[i-27,8]:
                    print(gpl[i,0],":",gpl[0,8],"--",gpl[i,8],"奖励一样了")

                #比对奖励名称
                if gpl[i,10] == gpl[i-27,10]:
                    if str(gpl[i,10]) != "nan":
                        print(gpl[i,0],":",gpl[0,10],"--",gpl[i,10],"奖励一样了")

                print("奖励头像框图标：",gpl[i,4])
                frame_icon = gpl[i,4] 
                print("奖励头像框id:",gpl[i,8])
                frame_id = gpl[i,8]
                print("奖励头像框名称:",gpl[i,10])
                frame_name = gpl[i,10]
                print("奖励头像框描述:",gpl[i,11])
                frame_des = gpl[i,11]
            elif i == lenth-5:
                #比对奖励icon
                if gpl[i,4] == gpl[i-27,4]:
                    if str(gpl[i,4]) != "nan":
                        print(gpl[i,0],":",gpl[0,4],"--",gpl[i,4],"奖励一样了")

                #比对VIP奖励
                if gpl[i,8] == gpl[i-27,8]:
                    print(gpl[i,0],":",gpl[0,8],"--",gpl[i,8],"奖励一样了")

                #比对奖励名称
                if gpl[i,10] == gpl[i-27,10]:
                    if str(gpl[i,10]) != "nan":
                        print(gpl[i,0],":",gpl[0,10],"--",gpl[i,10],"奖励一样了")
                print("奖励皮肤图标：",gpl[i,4])
                skin_icon = gpl[i,4]
                print("奖励皮肤id:",gpl[i,8])
                skin_id = gpl[i,8]
                print("奖励皮肤名称:",gpl[i,10])
                skin_name = gpl[i,10]
                print("奖励皮肤描述:",gpl[i,11])
                skin_des = gpl[i,11]
            else:
                #比对奖励icon
                if gpl[i,4] != gpl[i-27,4]:
                    if str(gpl[i,4]) != "nan":
                        print(gpl[i,0],":",gpl[0,4],"--",gpl[i,4])

                #比对VIP奖励
                if gpl[i,8] != gpl[i-27,8]:
                    print(gpl[i,0],":",gpl[0,8],"--",gpl[i,8])

                #比对奖励名称
                if gpl[i,10] != gpl[i-27,10]:
                    if str(gpl[i,10]) != "nan":
                        print(gpl[i,0],":",gpl[0,10],"--",gpl[i,10])

                #比对奖励描述
                if gpl[i,11] != gpl[i-27,11]:
                    if str(gpl[i,11]) != "nan":
                        print(gpl[i,0],":",gpl[0,11],"--",gpl[i,11])
gpid = gpl[-1,2]
print("\n")

activity = pd.read_excel("{f}\\ActivityTemplate.xlsx".format(f=Config.FILE_PATH))
act = activity.values
lenth_act = len(act)
for i in range(3,lenth_act):
    if act[i,0] == gpid:
        print("上期活动开启时间：",act[i-1,9])
        print("上期活动结束时间：",act[i-1,11])
        print("活动开启时间：",act[i,9])
        start_time = act[i,9]
        print("活动结束时间：",act[i,11])

frame = pd.read_excel("{f}\\FrameTemplate.xlsx".format(f=Config.FILE_PATH))
fra = frame.values

lenth_fra = len(fra)

for i in range(3,lenth_fra):
    if fra[i,0] == json.loads(frame_id)[0]:
        if fra[i,2] != frame_name:
            print("frameTemplate:头像框名称不一致",fra[i,0],fra[i,2])
        if fra[i,4] != frame_icon:
            print("frameTemplate:头像框icon不一致",fra[i,0],fra[i,4])
        if fra[i,8] != start_time:
            print("frameTemplate:头像框开启时间不一致",fra[i,0],fra[i,8])
        frame_t_des = fra[i,3]

skinTemplate = pd.read_excel("{f}\\SkinTemplate.xlsx".format(f=Config.FILE_PATH))

skin = skinTemplate.values

lenth_skin = len(skinTemplate)
skin_users = {"Petdragon","Femaleplayer"}
skin_types = {1,2}
for i in range(3,lenth_skin):
    if skin[i,0] == json.loads(skin_id)[0]:
        if skin[i,5] not in skin_users:
            print("skinTemplate:皮肤使用对象错误",skin[i,0],skin[i,5])
        if skin[i,2] != skin_name:
            print("skinTemplate:皮肤名称错误",skin[i,0],skin[i,2])
        if skin[i,4] not in skin_types:
            print("skinTemplate:皮肤类型错误",skin[i,0],skin[i,4])
        if skin[i,6] != skin_icon:
            print("skinTemplate:皮肤icon错误",skin[i,0],skin[i,6])
        if skin[i,11] != start_time:
            print("skinTemplate:皮肤时间错误",skin[i,0],skin[i,11])
        skin_t_des = skin[i,3]


itemTemplate = pd.read_excel("{f}\\ItemTemplate.xlsx".format(f=Config.FILE_PATH))

item = itemTemplate.values

lenth_item = len(item)

for i in range(3,lenth_item):
    if item[i,0] == json.loads(frame_id)[0]:
        if item[i,2] != frame_name:
            print("ItemTemplate:头像框名称不一致",item[i,0],item[i,2])
        if item[i,3] != frame_t_des:
            print("ItemTemplate\\frameTemplate:头像框描述不一致")
        if item[i,4] != frame_icon:
            print("ItemTemplate:头像框icon不一致",item[i,0],item[i,4])
        if item[i,26] != frame_id:
            print("ItemTemplate:头像框道具与发放的头像框不一致",item[i,0],item[i,26])

    if item[i,0] == json.loads(skin_id)[0]:
        if item[i,2] != skin_name:
            print("ItemTemplate:皮肤名称不一致",item[i,0],item[i,2])
        if item[i,3] != skin_t_des:
            print("ItemTemplate\\frameTemplate:皮肤描述不一致")
        if item[i,4] != skin_icon:
            print("ItemTemplate:皮肤icon不一致",item[i,0],item[i,4])
        if item[i,26] != skin_id:
            print("ItemTemplate:皮肤道具与发放的皮肤不一致",item[i,0],item[i,26])


configTemplate = pd.read_excel("{f}\\ConfigTemplate.xlsx".format(f=Config.FILE_PATH))

cfg = configTemplate.values

lenth_cfg = len(cfg)

for i in range(3,lenth_cfg):
    if cfg[i,0] == "goldPassPerk":
        vv = set()
        for j in json.loads(cfg[i,2]):
            vv.add(tuple(j))
        ww = {(gpid,1,2,5,3),(gpid-1,1,2,5,3),(gpid-2,1,2,5,3)}
        if vv != ww:
            print("config:黄金通行证特权配置错误",cfg[i,0])
    
    if cfg[i,0] == "goldPassIntegralBuffValue":
        vv = set()
        for j in json.loads(cfg[i,2]):
            vv.add(tuple(j))
        ww = {(gpid,1200),(gpid-1,1200),(gpid-2,1200)}
        if vv != ww:
            print("config:黄金通行证特权配置错误",cfg[i,0])
    
    if cfg[i,0] == "goldPassCovertGoldValue":
        vv = set()
        for j in json.loads(cfg[i,2]):
            vv.add(tuple(j))
        ww = {(gpid,1000),(gpid-1,1000),(gpid-2,1000)}
        if vv != ww:
            print("config:黄金通行证特权配置错误",cfg[i,0])
    
    if cfg[i,0] == "goldPassFileIndex":
        vv = set()
        print("config:检测通行证配置",cfg[i,2],gpid)









# %%
