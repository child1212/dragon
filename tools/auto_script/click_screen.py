import time
import os
a,b = int(input("x:")),int(input("y:"))
while True:
    os.system("adb shell input tap {a} {b}".format(a=a,b=b))