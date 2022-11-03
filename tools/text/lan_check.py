#%%
#检测多语言格式，是否有参数配置错误
names = ('AI','Dialog','Dragon','Guide','Obstacle','Pops','Story','SystemErrorCode','Tips','UI')
countries = ('ar','de','en','fr','it','ja','ko','ne','po','ru','sp','tc','th','tu','vi','zh')
for country in countries:
    print("#===================="+country+"=======================#")
    for name in names:
        lan = open("D:\\town\\dragon\\client\\client\\Assets\\HomeLand\\Localization\\{country}\\{name}.bytes".format(country=country,name=name),"r",encoding="utf-8")

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
    for name in names:
        lan = open("D:\\town\\dragon\\client\\client\\Assets\\HomeLand\\Localization\\{country}\\{name}.bytes".format(country=country,name=name),"r",encoding="utf-8")

        for line in lan:
            for lett in line:
                if "\u4e00" < lett <"\u9fff":
                    print(line)
                    break
        lan.close()
# %%
#检测参数首字母大写
names = ('AI','Dialog','Dragon','Guide','Obstacle','Pops','Story','SystemErrorCode','Tips','UI')
countries = ('ar','de','en','fr','it','ja','ko','ne','po','ru','sp','tc','th','tu','vi','zh')
for country in countries:
    print("#===================="+country+"=======================#")
    for name in names:
        lan = open("D:\\town\\dragon\\client\\client\\Assets\\HomeLand\\Localization\\{country}\\{name}.bytes".format(country=country,name=name),"r",encoding="utf-8")
        f_l = ('{Q','{W','{E','{R','{T','{Y','{U','{I','{O','{P','{A','{S','{D','{F','{G','{H','{J','{K','{L','{Z','{X','{C','{V','{B','{N','{M')
        for line in lan:
            for u in f_l:
                if u in line:
                    print(line)
                    break
        lan.close()
