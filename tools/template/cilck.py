#%%
import os

x=''
while x == '':
    # # 向右切换伙伴按钮
    os.system("adb shell input tap 978 548")
    x = input("")


