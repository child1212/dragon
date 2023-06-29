#%%
#首先使用filename.bat创建文件名列表
#编辑list.txt
#创建批处理命令
#执行批处理list.bat
#获得python库

import os
path_n = os.path.dirname(__file__)    #获取当前路径
path_r = "{a}\\package".format(a=os.path.dirname(path_n))    #获取上一级路径
l = open("list.txt", "r")
bat = open("list.bat", "w")
for line in l:
    if "proto" in line:
        bat.write("protoc -I={path_n} --python_out={path_r} {path_n}\\{line}".format(path_n=path_n,path_r=path_r, line=line))

l.close()
bat.close()
# %%
