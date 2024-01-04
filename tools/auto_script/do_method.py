#%%
import os
from time import sleep

# os.system("adb shell wm size 1080x2400")

def click(x,y):
    os.system("adb shell input tap {x} {y}".format(x=x, y=y))

def swipe(x1,y1,x2,y2):
    os.system("adb shell input swipe {x1} {y1} {x2} {y2} 2000".format(x1=x1, y1=y1, x2=x2, y2=y2))


def swipe_k(x1,y1,x2,y2):
    os.system("adb shell input swipe {x1} {y1} {x2} {y2} 200".format(x1=x1, y1=y1, x2=x2, y2=y2))

xa,xb,xc,xd = 1683,1935,2186,2431
ya,yb,yc = 579,923,1241




while True:
    click(xa,ya)
    swipe(480,423,1000,450)
    click(xb,ya)
    swipe(1000,423,480,450)
    click(xc,ya)
    swipe(480,423,1000,450)
    click(xd,ya)
    swipe(1000,423,480,450)
    click(xa,yb)
    swipe(480,423,1000,450)
    click(xb,yb)
    swipe(1000,423,480,450)
    click(xc,yb)
    swipe(480,423,1000,450)
    click(xd,yb)
    swipe(1000,423,480,450)
    click(xa,yc)
    swipe(480,423,1000,450)
    click(xb,yc)
    swipe(1000,423,480,450)
    click(xc,yc)
    swipe(480,423,1000,450)
    click(xd,yc)
    swipe(1000,423,480,450)
    # click(1306,700)
    # swipe(480,423,1000,450)
    # click(1512,700)
    # swipe(1000,423,480,450)
    # click(1696,700)
    # swipe(480,423,1000,450)
    # click(1888,700)
    # swipe(1000,423,480,450)
    # click(1306,850)
    # swipe(480,423,1000,450)
    # click(1512,850)
    # swipe(1000,423,480,450)
    # click(1696,850)
    # swipe(480,423,1000,450)
    # click(1888,850)
    # swipe(1000,423,480,450)
    # swipe(1888,702,1888,450)
    # swipe(1888,702,1888,450)
    # swipe(1888,690,1888,450)
    input("Enter")



# %%
