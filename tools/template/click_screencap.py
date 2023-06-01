#%%
import os
import json

with open("D:\\pyprogram\\PyTestTools\\dragon\\tools\\template\\config.json","r") as load_f:
    config = json.load(load_f)
num = config.get("num")
running=''
while running == '':
    os.system("adb exec-out screencap -p > e://screenshot/partner/partner_{num}.jpg".format(num=num))
    num += 1
    config["num"] = num
    load = json.dumps(config)
    with open("D:\\pyprogram\\PyTestTools\\dragon\\tools\\template\\config.json","w") as load_ff:
        load_ff.write(load)
    # os.system("adb -d exec-out screencap -p >e://screenshot/NFAERROR.jpg")
    running = input("continue?")





# %%
