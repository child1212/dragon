#%%
import os
from time import sleep

os.system("adb shell wm size 1080x2400")

def click(x,y):
    os.system("adb shell input tap {x} {y}".format(x=x, y=y))

def swipe(x1,y1,x2,y2):
    os.system("adb shell input swipe {x1} {y1} {x2} {y2} 2000".format(x1=x1, y1=y1, x2=x2, y2=y2))

def swipe_k(x1,y1,x2,y2):
    os.system("adb shell input swipe {x1} {y1} {x2} {y2} 200".format(x1=x1, y1=y1, x2=x2, y2=y2))

while True:
    click(1306,450)
    swipe(480,423,999,450)
    click(1512,450)
    swipe(999,423,480,450)
    click(1696,450)
    swipe(480,423,999,450)
    click(1888,450)
    swipe(999,423,480,450)
    click(1306,700)
    swipe(480,423,999,450)
    click(1512,700)
    swipe(999,423,480,450)
    click(1696,700)
    swipe(480,423,999,450)
    click(1888,700)
    swipe(999,423,480,450)
    click(1306,850)
    swipe(480,423,999,450)
    click(1512,850)
    swipe(999,423,480,450)
    click(1696,850)
    swipe(480,423,999,450)
    click(1888,850)
    swipe(999,423,480,450)
    # swipe(1888,702,1888,450)
    # swipe(1888,702,1888,450)
    # swipe(1888,690,1888,450)
    input("Enter")



# %%
