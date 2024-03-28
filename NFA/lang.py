# %%
#检测中文字符
print("检测中文字符")
names = ('AI','Dialog','Guide','Pops','Story','SystemErrorCode','Tips','UI','Partnerbubble')
countries = {'en','de','en','fr','it','sp','ko'}
for country in countries:
    print("#===================="+country+"=======================#")
    exc = ("errorcode_18004","errorcode_18005")
    for name in names:
        lan = open("E:\\FA\\client\\client\\Assets\\HomeLand\\Localization\\{country}\\{name}.bytes".format(country=country,name=name),"r",encoding="utf-8")

        for line in lan:
            if "errorcode_18004" in line or "errorcode_18005" in line:
                pass
            else:
                for lett in line:
                    if "\u4e00" < lett <"\u9fff":
                        print(line)
                        break
        lan.close()






print("检测参数配置和中文不一致的情况")
#检测参数配置和中文不一致的情况
#创建映射
names = ('AI','Dialog','Guide','Pops','Story','SystemErrorCode','Tips','UI','Partnerbubble')
countries = {'en','de','en','fr','it','ja','ko','sp','zh','tc'}
for country in countries:
    for name in names:
        lan = open("E:\\FA\\client\\client\\Assets\\HomeLand\\Localization\\{country}\\{name}.bytes".format(country=country,name=name),"r",encoding="utf-8")
        val = open("E:\\PyTools\\dragon\\NFA\\local\\{country}_{name}.txt".format(country=country,name=name),"w",encoding="utf-8")
        for line in lan:
            if "{" in line:
                keys = line.split("=")
                key = keys[0]
                te = ''
                run =[]
                for le in line:
                    if le == "{":
                        run.append(1)
                    elif le == "}":
                        run.pop() 
                        te += le+","
                    if len(run) > 0:
                        te += le
                val.write(key+":"+te+"\n")

        lan.close()
        val.close()

#执行比对
val = open("E:\\PyTools\\dragon\\NFA\\local\\zh_UI.txt".format(name=name),"r",encoding="utf-8")
stand = {}
for line in val:
    kx = line.split(':')
    kk = kx[1].split(",")
    kr = set(kk)
    stand[kx[0]] = kr
val.close()
# countries = ('ar','de','en','fr','it','ja','ko','ne','po','ru','sp','tc','th','tu','vi','zh')
countries = {'en','de','en','fr','it','ja','ko','sp','tc'}
for country in countries:
    print("#===================="+country+"=======================#")
    comp = {}
    lan = open("E:\\PyTools\\dragon\\NFA\\local\\{country}_UI.txt".format(country=country),"r",encoding="utf-8")
    for line in lan:
        kx = line.split(':')
        kk = kx[1].split(",")
        kr = set(kk)
        comp[kx[0]] = kr
    lan.close()
    for k in stand:
        if k in comp:
            if stand[k] != comp[k]:
                print(k)
        else:
            print("keylose:"+k)







print("检测多语言丢失key的情况")
# 检测多语言丢失key的情况
names = ('AI','Dialog','Guide','Pops','Story','SystemErrorCode','Tips','UI',"Partnerbubble")
countries = {'en','de','en','fr','it','sp','zh',"tc"}



for name in names:
    print("\n#####################"+name+"########################")
    for country in countries:
        val = open("E:\\PyTools\\dragon\\NFA\\local\\{country}_{name}.txt".format(country=country,name=name),"w",encoding="utf-8")
        lan = open("E:\\FA\\client\\client\\Assets\\HomeLand\\Localization\\{country}\\{name}.bytes".format(country=country,name=name),"r",encoding="utf-8")
        for line in lan:
            keys = line.split("=")
            val.write(keys[0]+"\n")
        lan.close()
        val.close()
    #创建对照库
    val = open("E:\\PyTools\\dragon\\NFA\\local\\zh_{name}.txt".format(name=name),"r",encoding="utf-8")
    stand = set()
    for line in val:
        line = line.replace("\n",'')
        if line in stand:
            print(line)
        else:
            stand.add(line)
    val.close()
    # 开始对比
    countries_compare = {'en','de','en','fr','it','sp','tc'}
    for country in countries_compare:
        print("#===================="+country+"=======================#")
        comp = set()
        lan = open("E:\\PyTools\\dragon\\NFA\\local\\{country}_{name}.txt".format(country=country,name=name),"r",encoding="utf-8")
        for line in lan:
            line = line.replace("\n",'')
            comp.add(line)
        for k in stand:
            if k in comp:
                pass
            else:
                    print(k)
        lan.close()




# %%
# %%
# #检测参数首字母大写
# names = ('AI','Dialog','Dragon','Guide','Obstacle','Pops','Story','SystemErrorCode','Tips','UI')
# countries = ('ar','de','en','fr','it','ja','ko','ne','po','ru','sp','tc','th','tu','vi','zh')
# for country in countries:
#     print("#===================="+country+"=======================#")
#     for name in names:
#         lan = open("E:\\town\\dragon\\client\\client\\Assets\\HomeLand\\Localization\\{country}\\{name}.bytes".format(country=country,name=name),"r",encoding="utf-8")
#         f_l = ('{Q','{W','{E','{R','{T','{Y','{U','{I','{O','{P','{A','{S','{D','{F','{G','{H','{J','{K','{L','{Z','{X','{C','{V','{B','{N','{M')
#         ig = {'UI_personaldata_short2','ui_AdventureGift_des','ui_goldpass_task_49','ui_goldpass_task_50','ui_goldpass_task_55'}
#         for line in lan:
#             for u in f_l:
#                 if u in line:
#                     r = 1
#                     for i in ig:
#                         if i in line:
#                             r=0
#                     if r != 0:
#                         print(line)
#                         break
#         lan.close()
#%%
#筛选dragon
names = ('AI','Dialog','Guide','Pops','Story','SystemErrorCode','Tips','UI','Partnerbubble')
countries = {'en',"it"}
for country in countries:
    print("#===================="+country+"=======================#")
    exc = ("errorcode_18004","errorcode_18005")
    for name in names:
        lan = open("E:\\FA\\client\\client\\Assets\\HomeLand\\Localization\\{country}\\{name}.bytes".format(country=country,name=name),"r",encoding="utf-8")

        for line in lan:
            r = line.split('=')
            if "Cynthia" in r[-1]:
                print(r[0])
        lan.close()

# %%
names = ('AI','Dialog','Guide','Pops','Story','SystemErrorCode','Tips','UI',"Partnerbubble")
countries = {'en','de','en','fr','it','sp','zh'}
for country in countries:
    print("#===================="+country+"=======================#")
    exc = ("errorcode_18004","errorcode_18005")
    for name in names:
        lan = open("E:\\FA\\client\\client\\Assets\\HomeLand\\Localization\\{country}\\{name}.bytes".format(country=country,name=name),"r",encoding="utf-8")

        for line in lan:
            r = line.split('=')
            x = r[-1].replace(' ','').replace('\n','')
            if x[-1] == ',' or x[-1] == '，':
                print(r[0])
        lan.close()
