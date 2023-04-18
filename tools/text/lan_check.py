#%%
#检测多语言格式，是否有参数配置错误
names = ('AI','Dialog','Dragon','Guide','Obstacle','Pops','Story','SystemErrorCode','Tips','UI')
countries = ('ar','de','en','fr','it','ja','ko','ne','po','ru','sp','tc','th','tu','vi','zh')
for country in countries:
    print("#===================="+country+"=======================#")
    for name in names:
        lan = open("E:\\town\\dragon\\client\\client\\Assets\\HomeLand\\Localization\\{country}\\{name}.bytes".format(country=country,name=name),"r",encoding="utf-8")

        l_k = ("a","b","c","d","e","f","g","h","i",'j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','_')
        l_a = ("a","b","c","d","e","f","g","h","i",'j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','_','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M')
        l_c = ('s','i','z','e','c','o','l','r','/','=','#','0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F',"a","b","c","d","e","f")
        for line in lan:
            t = []
            x = 0
            for lett in line:
                if lett == "{":
                    t.append(1)
                elif lett == "}":
                    try:
                        x = t.pop()
                    except:
                        x = 0
                    if x == 1:
                        x = 0
                    else:
                        print(line)
                elif lett == "<":
                    t.append(2)
                elif lett == ">":
                    try:
                        x = t.pop()
                    except:
                        x = 0
                    if x == 2:
                        x = 0
                    else:
                        print(line)
                else:
                    if len(t) > 0:
                        if t[-1] == 1:
                            if lett not in l_a:
                                print(line)
                                break
                        elif t[-1] == 2:
                            if lett not in l_c:
                                print(line)
                                break
        lan.close()
# %%
#检测中文字符
names = ('AI','Dialog','Dragon','Guide','Obstacle','Pops','Story','SystemErrorCode','Tips','UI')
countries = ('ar','de','en','fr','it','ko','ne','po','ru','sp','th','tu','vi')
for country in countries:
    print("#===================="+country+"=======================#")
    exc = ("errorcode_18004","errorcode_18005")
    for name in names:
        lan = open("E:\\town\\dragon\\client\\client\\Assets\\HomeLand\\Localization\\{country}\\{name}.bytes".format(country=country,name=name),"r",encoding="utf-8")

        for line in lan:
            if "errorcode_18004" in line or "errorcode_18005" in line:
                pass
            else:
                for lett in line:
                    if "\u4e00" < lett <"\u9fff":
                        print(line)
                        break
        lan.close()

# %%
#检测参数配置和中文不一致的情况
#创建映射
names = ('Story','UI')
countries = ('ar','de','en','fr','it','ja','ko','ne','po','ru','sp','tc','th','tu','vi','zh')
for country in countries:
    for name in names:
        lan = open("E:\\town\\dragon\\client\\client\\Assets\\HomeLand\\Localization\\{country}\\{name}.bytes".format(country=country,name=name),"r",encoding="utf-8")
        val = open("D:\\pyprogram\\PyTestTools\\dragon\\tools\\text\\local\\{country}_{name}.txt".format(country=country,name=name),"w",encoding="utf-8")
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
val = open("D:\\pyprogram\\PyTestTools\\dragon\\tools\\text\\local\\zh_UI.txt".format(name=name),"r",encoding="utf-8")
stand = {}
for line in val:
    kx = line.split(':')
    kk = kx[1].split(",")
    kr = set(kk)
    stand[kx[0]] = kr
val.close()
# countries = ('ar','de','en','fr','it','ja','ko','ne','po','ru','sp','tc','th','tu','vi','zh')
countries = ('de','en','fr','it','ja','ko','sp')
for country in countries:
    print("#===================="+country+"=======================#")
    comp = {}
    lan = open("D:\\pyprogram\\PyTestTools\\dragon\\tools\\text\\local\\{country}_UI.txt".format(country=country),"r",encoding="utf-8")
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





# %%
# 检测多语言丢失key的情况

names = ('AI','Dialog','Dragon','Guide','Obstacle','Pops','Story','SystemErrorCode','Tips','UI')
# names = ('Story','UI')
countries = ('ar','de','en','fr','it','ja','ko','ne','po','ru','sp','tc','th','tu','vi','zh')


for name in names:
    print("\n#####################"+name+"########################")
    for country in countries:
        val = open("D:\\pyprogram\\PyTestTools\\dragon\\tools\\text\\local\\{country}_{name}.txt".format(country=country,name=name),"w",encoding="utf-8")
        lan = open("E:\\town\\dragon\\client\\client\\Assets\\HomeLand\\Localization\\{country}\\{name}.bytes".format(country=country,name=name),"r",encoding="utf-8")
        for line in lan:
            keys = line.split("=")
            val.write(keys[0]+"\n")
        lan.close()
        val.close()
    #创建对照库
    val = open("D:\\pyprogram\\PyTestTools\\dragon\\tools\\text\\local\\zh_{name}.txt".format(name=name),"r",encoding="utf-8")
    stand = set()
    for line in val:
        line = line.replace("\n",'')
        if line in stand:
            print(line)
        else:
            stand.add(line)
    val.close()
    # 开始对比
    countries_compare = ('de','en','fr','it','ja','ko','sp')
    for country in countries_compare:
        print("#===================="+country+"=======================#")
        comp = set()
        lan = open("D:\\pyprogram\\PyTestTools\\dragon\\tools\\text\\local\\{country}_{name}.txt".format(country=country,name=name),"r",encoding="utf-8")
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
# 下方为CN用
# %%
# 检测英文

names = ('AI','Dialog','Dragon','Guide','Obstacle','Pops','Story','SystemErrorCode','Tips','UI')
# names = ('Story','UI')
countries = {'zh'}

ku = open("D:\\pyprogram\\PyTestTools\\dragon\\tools\\text\\ciku.txt",'r',encoding='utf-8-sig')
ku = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
ku = ",<>?;':\"{{}}[]\\|!@#$^*_`"
ku = {"魂魄","杀死","砍死","猎杀"}
for name in names:
    print("\n#####################"+name+"########################")
    for country in countries:
        lan = open("E:\\town\\dragon\\client\\client\\Assets\\HomeLand\\Localization\\{country}\\{name}.bytes".format(country=country,name=name),"r",encoding="utf-8")
        for line in lan:
            keys = line.split("=")
            for p in ku:
                p = p.replace("\n",'')
                x = keys[1]
                run = 1
                word = ''
                for i in x:
                    if i == '{' or i == '<':
                        run = 0
                    if run == 1:
                        word += i
                    if i == "}"or i == '>':
                        run = 1
                if p in word:
                    print(line)
                    break
        lan.close()


# %%
# 检测连续的标点
names = ('AI','Dialog','Dragon','Guide','Obstacle','Pops','Story','SystemErrorCode','Tips','UI')
# names = ('Story','UI')
countries = {'zh'}

ku = "！@#￥%……&*（）——+？/》《【】》？、=-·~“”’‘；："
for name in names:
    print("\n#####################"+name+"########################")
    for country in countries:
        lan = open("E:\\town\\dragon\\client\\client\\Assets\\HomeLand\\Localization\\{country}\\{name}.bytes".format(country=country,name=name),"r",encoding="utf-8")
        for line in lan:
            keys = line.split("=")
            # for p in ku:
            #     p = p.replace("\n",'')
            x = keys[1]
            run = 1
            word = ''
            for i in x:
                if i == '{' or i == '<':
                    run = 0
                if run == 1:
                    word += i
                if i == "}"or i == '>':
                    run = 1
            for index in range(len(word)):
                if word[index] in ku and word[index+1] in ku and word[index] != "…":
                    print(line)
                    break

        lan.close()


# %%
# 检测句子末尾没有标点

names = ('AI','Dialog','Dragon','Guide','Obstacle','Pops','Story','SystemErrorCode','Tips','UI')
# names = ('Story','UI')
countries = {'zh'}

ku = open("D:\\pyprogram\\PyTestTools\\dragon\\tools\\text\\ciku.txt",'r',encoding='utf-8-sig')
ku = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
ku = "！。？…"
for name in names:
    print("\n#####################"+name+"########################")
    for country in countries:
        lan = open("E:\\town\\dragon\\client\\client\\Assets\\HomeLand\\Localization\\{country}\\{name}.bytes".format(country=country,name=name),"r",encoding="utf-8")
        for line in lan:
            keys = line.split("=")
            ke = keys[1].replace("\n","")
            if "\u4e00" < ke[-1] <"\u9fff":
                print(line)
        lan.close()

#"\u4e00" < ke[-1] <"\u9fff" or

# %%
# 检测标点处换行

names = ('AI','Dialog','Dragon','Guide','Obstacle','Pops','Story','SystemErrorCode','Tips','UI')
# names = ('Story','UI')
countries = {'zh'}

ku = open("D:\\pyprogram\\PyTestTools\\dragon\\tools\\text\\ciku.txt",'r',encoding='utf-8-sig')
ku = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
ku = "！。？…，"
for name in names:
    print("\n#####################"+name+"########################")
    for country in countries:
        lan = open("E:\\town\\dragon\\client\\client\\Assets\\HomeLand\\Localization\\{country}\\{name}.bytes".format(country=country,name=name),"r",encoding="utf-8")
        for line in lan:
            keys = line.split("=")
            ke = keys[1].replace("\n","")
            if len(ke) >= 45:
                if ke[44] in ku:
                # if "原住民" in ke:
                    print(line)
        lan.close()
