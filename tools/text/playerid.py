#%%
f = open("C:\\Users\\Administrator\\Downloads\\repair.log",'r',encoding="utf-8")
ff = open("C:\\Users\\Administrator\\Downloads\\repair.txt",'w',encoding="utf-8")

for line in f:
    line = line.replace(" ",'').replace("\n",'')
    if len(line) > 4:
        ff.write(line)
f.close()

ff.close()
# %%
