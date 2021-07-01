#%%
#首先使用filename.bat创建文件名列表
#编辑list.txt
#创建批处理命令
#执行批处理获得python库

import os
path_n = os.getcwd()    #获取当前路径

l = open("list.txt", "r")
bat = open("list.bat", "w")
for line in l:
    if "proto" in line:
        bat.write("protoc -I={path_n} --python_out={path_n} {path_n}\\{line}".format(path_n=path_n, line=line))

l.close()
bat.close()
# %%