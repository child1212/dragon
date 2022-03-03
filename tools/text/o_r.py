#%%


order = open("D:\\pyprogram\\PyTestTools\\dragon\\tools\\text\\order.txt",'r',encoding="utf-8")
points = open("D:\\pyprogram\\PyTestTools\\dragon\\tools\\text\\recharge.txt",'r',encoding="utf-8")
result = open("D:\\pyprogram\\PyTestTools\\dragon\\tools\\text\\result.txt",'w',encoding="utf-8")

gia = set()

for o_line in order:
    gia.add(o_line.replace(" ",""))

for point in points:
    gia.discard(point.replace(" ",""))

for i in gia:
    result.write(i)

order.close()
points.close()
result.close()
# %%