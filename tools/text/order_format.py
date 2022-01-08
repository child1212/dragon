#%%
order = open("D:\\pyprogram\\PyTestTools\\dragon\\tools\\text\\repair.log",'r',encoding="utf-8")
result = open("D:\\pyprogram\\PyTestTools\\dragon\\tools\\text\\result.txt",'w',encoding="utf-8")



for line in order:
    line = line.replace("\t"," ")
    # if "false" in line:
    #     result.write(line)
    result.write(line)



order.close()
result.close()

# %%
