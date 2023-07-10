#%%
import pandas as pd
import json

with open("data.json", "r") as f:
    data = json.load(f)
df = pd.read_excel('6.13-6.20.xlsx')

original_data = df.values
for line in original_data:
    if type(line[1]) != float:
        info = line[1].replace("\\","").replace(" ","").replace("n","").replace("=",":").replace(",}","}").replace('productId','"productId"').replace('orderId','"orderId"').replace('expired','"expired"').replace('1:','"1":').replace('2:','"2":').replace('3:','"3":').replace('4:','"4":')
        info = json.loads(info)
        for key in info:
            if info[key].get("orderId") != None:
                if data.get(info[key]["orderId"]) == None:
                    data[info[key]["orderId"]] = info[key]["expired"]
                elif data.get(info[key]["orderId"]) != info[key]["expired"]:
                    print(info[key]["orderId"],"订单时间错误")
                else:
                    pass





print(len(data))

    # running = input("")
    # if running == "1":
    #     break











with open("data.json", "w") as f:
    json.dump(data, f)



# %%
