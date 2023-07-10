#%%
#横版
#填写参数
x = '00000ab5'  #adb shell getevent -t -l  ABS_MT_POSITION_X   
y = '000006aa'  #adb shell getevent -t -l  ABS_MT_POSITION_Y
xmin = 0     
xmax = 4095  #adb shell getevent -p       0035
ymin = 0
ymax = 4095  #adb shell getevent -p       0036
width = 1080  #adb shell wm size
high = 2400


xx = int('{x}'.format(x=x),16)
yy = int('{y}'.format(y=y),16)
x0 = xx * width // xmax
y0 = yy * high // ymax

print(y0, width-x0)
# %%
#横版google手机
#填写参数
x = '000000b2'  #adb shell getevent -t -l  ABS_MT_POSITION_X   
y = '0000081a'  #adb shell getevent -t -l  ABS_MT_POSITION_Y
xmin = 0     
xmax = 1439  #adb shell getevent -p       0035
ymin = 0
ymax = 2959  #adb shell getevent -p       0036
width = 1440  #adb shell wm size
high = 2960


xx = int('{x}'.format(x=x),16)
yy = int('{y}'.format(y=y),16)
x0 = xx * width // xmax
y0 = yy * high // ymax

print(y0, width-x0)

# > input tap 169 640
# > input tap 1405 640
# > input tap 243 91
# > input tap 1671 1351
# > input tap 2144 1320


#91 634
#992 255
# %%