#%%
shoppack1=[[1001,220],[1003,100],[13001,5],[15000,5],[16000,5]]
shoppack2=[[1001,550],[1003,500],[16000,8],[25000,1]]
shoppack3=[[1001,1400],[1003,800],[11001,3],[16000,10],[25000,2]]
shoppack4=[[1001,4000],[1003,1500],[11001,10],[16000,20],[25000,5]]
shoppack5=[[1001,800],[2100,300],[13001,6],[15000,6],[16000,6]]
shoppack6=[[1001,5400],[1003,2800],[11001,20],[2100,80],[22000,30]]
defa = [[1001,3000]]
ui_coin_gift_1 = [[1001,-30],[1002,400],[13001,3],[15000,3],[16000,3]]
ui_coin_gift_2 = [[1001,-50],[1002,600],[2007,5],[2008,5],[22000,5]]
ui_coin_gift_3 = [[1001,-150],[1002,2400],[11001,1],[13001,10],[15000,10],[16000,10]]
ui_coin_gift_4 = [[1001,-300],[1002,5000],[11001,3],[13001,20],[15000,20],[16000,20]]


name = input("name:")
mine = {}


#创建奖品名称映射
table_item = open("D:\\pyprogram\\PyTestTools\\dragon\\tools\\ItemTemplate.csv","r",encoding="utf-8-sig")
item = {}
for line in table_item:
    line_l = line.split(",")
    item[str(line_l[0])] = line_l[1]
table_item.close()

while name != '':
    print(name,"============================")
    for reward in eval(name):
        if reward[0] in mine:
            mine[reward[0]] += reward[1]
        else:
            mine[reward[0]] = reward[1]
    for i in mine:
        print("{name}:{num}".format(name=item[str(i)],num=mine[i]))
    print(name,"============================\n")
    name = input("name:")




# %%
