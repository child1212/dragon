#%%
import win32gui
import win32api
import win32com.client
import win32con
import pythoncom
import time

# 获取窗口句柄
handle=win32gui.FindWindow(None, "雷电模拟器")
# 返还窗口信息（x,y坐标，还有宽度，高度）
handleDetail = win32gui.GetWindowRect(handle)
time.sleep(1)
win32gui.MoveWindow(handle, 0, 0, 1920, 1040, True)




# 模拟鼠标在(400, 500)位置进行点击操作
point = (930, 837)
win32api.SetCursorPos(point)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)






#%%
# 获取位置
point = win32api.GetCursorPos()
print(point)





























# %%
