#%%
from unittest import result


plantid = open("D:\\pyprogram\\PyTestTools\\dragon\\tools\\plantid.txt","r",encoding="utf-8-sig")
res = open("D:\\pyprogram\\PyTestTools\\dragon\\tools\\plantid_out.txt","w",encoding="utf-8-sig")
plant = set()


for line in plantid:
    line = line.replace("\n","")
    plant.add(line)
for i in plant:
    res.write('\\"{id}\\",'.format(id=i))



res.close()
plantid.close()

# %%
