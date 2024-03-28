#%%
import cv2 as cv
import numpy as np

imgs = ["l1.png","l2.png","l3.png","l4.png","l5.png","r1.png","r2.png","r3.png","r4.png","r5.png"]

img = cv.imread("E:\\screenshot\\NFA.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imwrite("gray.png",gray)
_, binary = cv.threshold(gray,220,255,cv.THRESH_BINARY)
cv.imwrite("binary.png",binary)
contours, hierarchy = cv.findContours(binary, cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
newimage = cv.imread("white.png")
newimage = cv.resize(newimage,(3000,3000))
cv.drawContours(newimage,contours,-1,(0,0,0),3)
cv.imshow("img",newimage)
cv.waitKey(0)






# %%
import cv2 as cv
import numpy as np
import os
os.system("adb -d exec-out screencap -p > e:/screenshot/NFA.jpg")

imgs = ["l1.png","l2.png","l3.png","l4.png","l5.png"]
for image in imgs:
    img = cv.imread(image)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    _, binary = cv.threshold(gray,220,255,cv.THRESH_BINARY)
    cv.imwrite("binary.png",binary)
    contours, hierarchy = cv.findContours(binary, cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    newimage = cv.imread("white.png")
    newimage = cv.resize(newimage,(3000,3000))


    img1 = cv.imread("E:\\screenshot\\NFA.jpg")
    gray1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
    _, binary1 = cv.threshold(gray1,220,255,cv.THRESH_BINARY)
    cv.imwrite("binary.png",binary1)
    contours1, hierarchy1 = cv.findContours(binary1, cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    match = cv.matchShapes(contours[0],contours1[0],1,0.0)
    # if match < 1.5:
    #     print(image)
    print(match)






#%%
import cv2 as cv
import numpy as np
import os
os.system("adb -d exec-out screencap -p > e:/screenshot/NFA.jpg")
img1 = cv.imread("E:\\screenshot\\NFA.jpg")
gray1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
_, binary1 = cv.threshold(gray1,220,255,cv.THRESH_BINARY)
cv.imwrite("binary.png",binary1)
contours1, hierarchy1 = cv.findContours(binary1, cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
print(contours1[0])




# %%
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

imgs = ["l1.png","l2.png","l3.png","l4.png","l5.png","r1.png","r2.png","r3.png","r4.png","r5.png"]

img = cv.imread("l0.png")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
w,h = gray.shape[::-1]


img1 = cv.imread("E:\\screenshot\\leidian.jpg")
gray1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)

match = cv.matchTemplate(gray,gray1,cv.TM_CCORR_NORMED)
print(cv.minMaxLoc(match))
min_val, max_val, min_loc, max_loc =cv.minMaxLoc(match)
top_left = max_loc
bottom_right = (top_left[0] + w,top_left[1] + h)
cv.rectangle(img1, top_left,bottom_right, (10,10,255), 5)
plt.imshow(img1)
# %%
