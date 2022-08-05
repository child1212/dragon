#%%
table_reward = open('D:\\pyprogram\\PyTestTools\\dragon\\tools\\text\\reward.txt',"r",encoding="utf-8-sig")
table_item = open("D:\\pyprogram\\PyTestTools\\dragon\\tools\\ItemTemplate.csv","r",encoding="utf-8-sig")

#创建奖品名称映射
item = {}
for line in table_item:
    line_l = line.split(",")
    item[str(line_l[0])] = line_l[1]

#统计奖励数量
for line in table_reward:
    reward = eval(line)
    while len(reward) < 2:
        reward.append(1)
    
    try:
        print("{name}:{num}".format(name=item[str(reward[0])],num=str(reward[1])))
    except:
        print(str(reward[0]),":",str(reward[1]))


    
table_reward.close()
table_item.close()
# %%
