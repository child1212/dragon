#%%
table_reward = open('D:\\pyprogram\\PyTestTools\\dragon\\tools\\text\\reward_name.txt',"r",encoding="utf-8-sig")
table_item = open("D:\\pyprogram\\PyTestTools\\dragon\\tools\\ItemTemplate.csv","r",encoding="utf-8-sig")

#创建奖品名称映射
item = {}
for line in table_item:
    line_l = line.split(",")
    item[str(line_l[0])] = line_l[1]

#统计奖励数量
for line in table_reward:
    line = line.replace("\n","")
    try:
        print("{name}".format(name=item[str(line)]),end="\n")
    except:
        print("no name")


    
table_reward.close()
table_item.close()
# %%
