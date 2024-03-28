#%%
import os
import sys
import inspect
import config

# def script_path():
#     this_file = inspect.getfile(inspect.currentframe())
#     path = os.path.abspath(os.path.dirname(this_file))
#     return path

# g_cur_dir               = script_path()
# g_prj_home              = os.path.normpath(os.path.join(g_cur_dir, "../"))
# g_client_home           = os.path.normpath(os.path.join(g_prj_home, "client"))
# g_external_home         = os.path.normpath(os.path.join(g_cur_dir, "../external"))
# g_script_home           = os.path.normpath(os.path.join(g_client_home, "Assets/HomeLand/LuaScript"))
# g_assets_home              = os.path.normpath(os.path.join(g_client_home, "Assets/"))
# g_art_home              = os.path.normpath(os.path.join(g_client_home, "Assets/HomeLand/"))
local_file_path = config.g_art_home

print("--检测中文字符--")
names = ('AI','Dialog','Guide','Pops','Story','SystemErrorCode','Tips','UI','Partnerbubble')
countries = {'ar','de','en','fr','it','ko','ne','po','ru','sp','th','tu','vi'}
for country in countries:
    print("#===================="+country+"=======================#")
    exc = ("errorcode_18004","errorcode_18005")
    for name in names:
        lan = open("{home}\\Localization\\{country}\\{name}.bytes".format(home=local_file_path,country=country,name=name),"r",encoding="utf-8")

        for line in lan:
            if "errorcode_18004" in line or "errorcode_18005" in line:
                pass
            else:
                for lett in line:
                    if "\u4e00" < lett <"\u9fff":
                        print(line)
                        break
        lan.close()


print("\n\n--检测参数配置和中文不一致的情况--")

names = ('AI','Dialog','Guide','Pops','Story','SystemErrorCode','Tips','UI','Partnerbubble')
countries = {'ar','de','en','fr','it','ja','ko','ne','po','ru','sp','zh','tc','th','tu','vi'}

local_values = {}
for country in countries:
    for name in names:
        lan = open("{home}\\Localization\\{country}\\{name}.bytes".format(home=local_file_path,country=country,name=name),"r",encoding="utf-8")
        local_values["{country}_{name}".format(country=country,name=name)] = []
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
                local_values["{country}_{name}".format(country=country,name=name)].append(key+":"+te)
        lan.close()

#执行比对
val = local_values["zh_UI"]
stand = {}
for line in val:
    kx = line.split(':')
    kk = kx[1].split(",")
    kr = set(kk)
    stand[kx[0]] = kr
# countries ={'ar','de','en','fr','it','ja','ko','ne','po','ru','sp','zh','tc','th','tu','vi'}
for country in countries:
    print("#===================="+country+"=======================#")
    comp = {}
    lan = local_values["{country}_UI".format(country=country)]
    for line in lan:
        kx = line.split(':')
        kk = kx[1].split(",")
        kr = set(kk)
        comp[kx[0]] = kr
    for k in stand:
        if k in comp:
            if stand[k] != comp[k]:
                print(k)
        else:
            print("keylose:"+k)


print("\n\n--检测多语言丢失key的情况--")
names = ('AI','Dialog','Guide','Pops','Story','SystemErrorCode','Tips','UI',"Partnerbubble")
countries = {'en','de','en','fr','it','sp','zh',"tc"}


local_var = {}
for name in names:
    print("\n#####################"+name+"########################")
    for country in countries:
        local_var["{country}_{name}".format(country=country,name=name)] = []
        lan = open("{home}\\Localization\\{country}\\{name}.bytes".format(home=local_file_path,country=country,name=name),"r",encoding="utf-8")
        for line in lan:
            keys = line.split("=")
            local_var["{country}_{name}".format(country=country,name=name)].append(keys[0])
        lan.close()
    #创建对照库
    val = local_var["zh_{name}".format(name=name)]
    stand = set()
    for line in val:
        line = line.replace("\n",'')
        if line in stand:
            print(line)
        else:
            stand.add(line)
    # 开始对比
    countries_compare = {'en','de','en','fr','it','sp','tc'}
    for country in countries_compare:
        print("#===================="+country+"=======================#")
        comp = set()
        lan = val = local_var["{country}_{name}".format(country=country,name=name)]
        for line in lan:
            line = line.replace("\n",'')
            comp.add(line)
        for k in stand:
            if k in comp:
                pass
            else:
                    print(k)

input("exit")

