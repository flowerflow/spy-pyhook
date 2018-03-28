# -*- coding: utf-8 -*-
import  os
import platform
import socket
from PyQt5.QtWidgets import QWidget, QApplication, QLabel,  QTableWidget,QHBoxLayout, QTableWidgetItem, QComboBox,QFrame
from PyQt5.QtGui import QFont,QColor,QBrush,QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets,Qt
import sys

class host():
    def __init__(self):



class Ui_MainWindow(object):
    def __init__(self):
        self.HOST = '127.0.0.1'
        self.PORTfileget = 10001
        self.PORTfilesend = 10002
        self.PORTmessageget = 10003
        self.PORTmessagesend = 10001

        self.messagein = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 定义socket类型，网络通信，TCP
        self.messagein.bind((self.HOST, self.messagein))  # 套接字绑定的IP与端口
        self.messagein.listen(5)

        self.messageout = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 定义socket类型，网络通信，TCP
        self.messageout.bind((self.HOST, self.messageout))  # 套接字绑定的IP与端口
        self.messageout.listen(5)

        self.filein = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 定义socket类型，网络通信，TCP
        self.filein.bind((self.HOST, self.PORTfileget))  # 套接字绑定的IP与端口
        self.filein.listen(5)

        self.fileout= socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 定义socket类型，网络通信，TCP
        self.fileout.bind((self.HOST, self.PORTfilesend))  # 套接字绑定的IP与端口
        self.fileout.listen(5)
        pass
    def setupUi(self, MainWindow):
        #设置字体
        hostname = socket.gethostname()
        hostname+=(' '+socket.gethostbyname(hostname))
        platos=platform.platform()
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        #窗口名字
        MainWindow.setObjectName("main")
        MainWindow.resize(678, 586)
        MainWindow.setWindowTitle("控制程序")

        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.onlinenum = QtWidgets.QLabel(self.centralWidget)
        self.onlinenum.setGeometry(QtCore.QRect(0, 10, 151, 21))
        self.onlinenum.setFont(font)
        self.onlinenum.setObjectName("onlinenum")
        self.onlinenum.setText("当前在线数：0")
        #在线数目


        #显示器
        self.table = QtWidgets.QTableWidget(self.centralWidget)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setGeometry(QtCore.QRect(10, 40, 301, 541))
        self.table.setRowCount(1)
        self.table.setColumnCount(2)
        self.table.setObjectName("table")
        item = QtWidgets.QTableWidgetItem()
        item.setText("本地(1)")
        self.table.setVerticalHeaderItem(0, item)



        item = QtWidgets.QTableWidgetItem()
        item.setText("地址")
        #设置头部，第一行，’地址‘
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("电脑信息")
        #设置头部，第二行，’电脑信息‘
        self.table.setHorizontalHeaderItem(1, item)
        self.table.verticalHeader().setHighlightSections(True)

        #设置单行
        self.table.setItem(0, 0, QTableWidgetItem(hostname))
        self.table.setItem(0,1,QTableWidgetItem(platos))

        #添加新行
        self.table.insertRow(1)#插入到第2行，前提是第一行要存在
        self.table.setItem(1, 1, QTableWidgetItem(platos))

        self.table.insertRow(2)#插入到第3行，前提是第一行要存在
        self.table.setItem(2, 1, QTableWidgetItem(platos))

        #删除
        #self.table.removeRow(0)#删除第一行

        #添加动作事件
        self.table.cellDoubleClicked.connect(self.onDockListIndexChanged)#双击
        self.table.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)  ######允许右键产生子菜单
        self.table.customContextMenuRequested.connect(self.shubiaoyoujian)  ####右键菜单

        #反馈信息台
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(310, 10, 351, 231))
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.label.setText("信息")

        #cmd命令台
        self.textEdit = QtWidgets.QTextEdit(self.centralWidget)
        self.textEdit.setGeometry(QtCore.QRect(310, 310, 331, 221))
        self.textEdit.setObjectName("textEdit")

        #提交按钮
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(560, 540, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Go")
        #############需要添加提交事件#####################
        MainWindow.setCentralWidget(self.centralWidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def shuangxininfo(self):
        #这里需要刷新控制台信息
        pass
    def   tijiaocmd(self,n):
        #这里需要提交命令
        pass
    def threadall(self):
        #这里把所有监听线程全开了
        pass

    def shubiaoyoujian(self,index):
        #鼠标右键事件
        point = self.table.indexAt(index)
        print(QtCore.QModelIndex.row(point),QtCore.QModelIndex.column(point))

    def onDockListIndexChanged(self, row,line):
        #双击事件
        print(row,line)
    def deletepc(self,n):
        #删除某个下线的机器
        pass
    def addnewpc(self,):
        #新的机器上线了
        pass




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

