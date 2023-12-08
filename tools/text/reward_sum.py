#%%
import pandas as pd
project = "NFA"
if project == "NFA":
    table_item = pd.read_excel("E:\\FA\\nfa-config\\excel\\DataFile\\ItemTemplate.xlsx")
    table_item = table_item.values
elif project == "DFA":
    table_item = pd.read_excel("E:\\dragon\\dragon-config\\excel\\DataFile\\ItemTemplate.xlsx")
    table_item = table_item.values
temp = open('E:\\PyTools\\dragon\\tools\\text\\reward.txt',"r",encoding="utf-8-sig")
rewards = []
for line in temp:
    x = eval(line)
    if type(x[0]) == list:
        for i in x:
            rewards.append(i)
    else:
        rewards.append(x)

temp.close()

#创建奖池
reward_num = {}
#统计奖励数量
for reward in rewards:
    while len(reward) < 2:
        reward.append(1)
    if str(reward[0]) in reward_num:
        reward_num[str(reward[0])] += reward[1]
    else:
        reward_num[str(reward[0])] = reward[1]
#创建奖品名称映射
item = {}
for line in table_item:
    item[line[0]] = line[1]

#打印奖品名称和数量
for key in reward_num:
    try:
        print("{name}:{num}".format(name=item[int(key)],num=reward_num[key]))
    except:
        print(key,":",reward_num[key])

# %%
