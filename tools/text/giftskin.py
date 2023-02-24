#%%
table_reward = open('D:\\pyprogram\\PyTestTools\\dragon\\tools\\text\\data\\reward.txt',"r",encoding="utf-8-sig")
table_item = open("D:\\pyprogram\\PyTestTools\\dragon\\tools\\ItemTemplate.csv","r",encoding="utf-8-sig")

#创建奖品名称映射
item = {}
for line in table_item:
    line_l = line.split(",")
    item[str(line_l[0])] = line_l[1]

#统计奖励数量
for line in table_reward:
    ll = line.split("\t")
    moment = ll[0]
    print(moment)
    reward = eval(ll[1])
    for r in reward:
        for s in r[1]:
            s[0] = item[str(s[0])]
        print(r)
    if input(''):
        break

    
table_reward.close()
table_item.close()
# %%
