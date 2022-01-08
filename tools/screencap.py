import os
N = True
name = 1
while N:
    os.system("adb exec-out screencap -p > E:/screenshot/{name}.jpg".format(name=name))
    name += 1
    x = input("N:")
    if x:
        N = False