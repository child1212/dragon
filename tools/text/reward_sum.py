#%%

#打开文件
table_reward = open('D:\\pyprogram\\PyTestTools\\dragon\\tools\\text\\reward.txt',"r",encoding="utf-8-sig")
table_item = open("D:\\pyprogram\\PyTestTools\\dragon\\tools\\ItemTemplate.csv","r",encoding="utf-8-sig")

#创建奖池
reward_num = {}
#统计奖励数量
for line in table_reward:
    reward = eval(line)
    while len(reward) < 2:
        reward.append(1)
    if str(reward[0]) in reward_num:
        reward_num[str(reward[0])] += reward[1]
    else:
        reward_num[str(reward[0])] = reward[1]
#创建奖品名称映射
item = {}
for line in table_item:
    line_l = line.split(",")
    item[str(line_l[0])] = line_l[1]

#打印奖品名称和数量
for key in reward_num:
    try:
        print("{name}:{num}".format(name=item[key],num=reward_num[key]))
    except:
        print(key,":",reward_num[key])
table_reward.close()
table_item.close()

# %%
