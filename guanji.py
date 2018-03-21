# -*- coding:utf-8 -*-
import time
import win32api
import win32con 
def guanji():
    print ("run")
    win32api.keybd_event(91, 0, 0, 0)
    win32api.keybd_event(88, 0, 0, 0)
    win32api.keybd_event(91, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(88, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(1)
    print "wait"
    win32api.keybd_event(85, 0, 0, 0)
    win32api.keybd_event(85, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(73, 0, 0, 0)
    win32api.keybd_event(73, 0, win32con.KEYEVENTF_KEYUP, 0)
    return True
guanji()