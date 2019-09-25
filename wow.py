
# -*- coding: UTF-8 -*-
# Python version: 3.4.0

# 安装pywin32模块 pip install pywin32
# 必须先登录战网

# 获取鼠标当前位置的坐标
# win32api.GetCursorPos()
# 将鼠标移动到坐标处
# win32api.SetCursorPos((200, 200))
# 左点击
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 200, 200, 0, 0)
# win32api.mouse_event(win32con.MUOSEEVENTF_LEFTUP, 200, 200, 0, 0)
# 获取窗口句柄
# win32gui.FindWindow(None, 'qq')
# win32gui.FindWindow('TXGuiFoundation', None)
# 通过坐标获取窗口句柄
# hw = win32gui.WindowFromPoint(win32api.GetCursorPos())
# 获取窗口classname
# win32gui.GetClassName(hw)
# 获取窗口标题
# win32gui.GetWindowText(hw)
# 获取窗口坐标
# win32gui.GetwindowRect(hw)



import win32gui, win32api, win32con,time
 
def closeWindow(name):
	win32gui.PostMessage(name, win32con.WM_CLOSE, 0, 0)


def LeftClick(x, y):    # 鼠标左键点击屏幕上的坐标(x, y)
    win32api.SetCursorPos((x, y))    # 鼠标定位到坐标(x, y)
    # 注意：不同的屏幕分辨率会影响到鼠标的定位，有需求的请用百分比换算
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)    # 鼠标左键按下
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)    # 鼠标左键弹起
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN + win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)    # 测试


 
def LeftDoubleClick(x, y):    # 鼠标左键点击屏幕上的坐标(x, y)
    win32api.SetCursorPos((x, y))    # 鼠标定位到坐标(x, y)
    # 注意：不同的屏幕分辨率会影响到鼠标的定位，有需求的请用百分比换算
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)    # 鼠标左键按下
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)    # 鼠标左键弹起
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)    # 鼠标左键按下
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)    # 鼠标左键弹起
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN + win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)    # 测试

def getWindow(titlename):    # 鼠标左键点击屏幕上的坐标(x, y)
	win32gui.FindWindow(None, titlename)
 
 
def PressOnce(x):    # 模拟键盘输入一个按键的值，键码: x
    win32api.keybd_event(x, 0, 0, 0)

def Enter(name): 
	#发送回车
	win32gui.PostMessage(name, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
	win32gui.PostMessage(name, win32con.WM_KEYUP, win32con.VK_RETURN, 0)
 
def maxWindows(name): 
	#全屏
	win32gui.ShowWindow(name, 0)
	win32gui.ShowWindow(name, 1)
	win32gui.ShowWindow(name,win32con.SW_MAXIMIZE)

# 测试
#LeftClick(30, 30)  # 我的电脑？
# PressOnce(13)  # Enter
# PressOnce(9)   # TAB

# t1=win32gui.GetDlgItem(wow,1412)
# t2=win32gui.GetDlgItem(wow,1)
#获取窗口左上角和右下角坐标 
# left, top, right, bottom = win32gui.GetWindowRect(wow)
# LeftClick()
def exec():
	classname = "Game"
	titlename = "暴雪战网"
	titlenamewow = "魔兽世界"
	#获取战网句柄
	battle=win32gui.FindWindow(None,titlename)
	wow=win32gui.FindWindow(None,titlenamewow)
	#关闭wow窗口
	#closeWindow(wow)
	#战网窗口最大化
	maxWindows(battle)
	#回车 启动wow
	#Enter(battle)
	time.sleep(2)
	maxWindows(wow)
	#选择服务器
	#servers = win32gui.FindWindowEx(wow, None, None,u'服务器选择')#获取hld下第一个为edit控件的句柄
	left, top, right, bottom = win32gui.GetWindowRect(wow)
	print(left)
	print(top)
	print(right)
	print(bottom)

exec() 