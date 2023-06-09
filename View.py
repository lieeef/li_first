# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 11:33:29 2023

@author: lenovo
"""
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
# import PyQt5.QtWidgets
# import time

# from lib.output import console
# from ipaddress import ip_address

# from plugins.Crawl.web_crawl import Crawl
# from plugins.Scan.active_scan import ActiveCheck

# # def display():
# def clickButton():
#     # app = QApplication(sys.argv)
#     win = QMainWindow()
#     win.setFixedSize(900,700)
#     # 设置窗口的标题栏
#     win.setWindowTitle('欢迎进入系统')
#     win.show()
#     # sys.exit(app.exec_())
    
# def clickButton1():
#     start_ip = input('使用主机存活扫描，请输入起始IP地址：')
#     end_ip = input('请输入终止IP地址：')
#     start_time = time.time()
#     active_hosts = ActiveCheck(findIPs(start_ip, end_ip), 'active_result').pool()
#     end_time = time.time()
#     print('\nrunning {0:.3f} seconds'.format(end_time - start_time))

# if __name__=='__main__':
#     #创建主窗口 
#     # 创建一个app主体
#     app = QApplication(sys.argv)
#     # 创建一个主窗口 
#     win = QMainWindow()
#     win.setFixedSize(300,200)
#     # 设置窗口的标题栏
#     win.setWindowTitle('登录')
    
#     win2 = QMainWindow()
#     win2.setFixedSize(900,700)
#     # 设置窗口的标题栏
#     win2.setWindowTitle('欢迎进入系统')
#     # 创建label，创建之初指定父亲
#     btn1 = QPushButton("主机存活扫描", win2)
#     # 显示位置与大小：(x, y, w, h)
#     btn1.setGeometry(20, 20, 150, 80)
#     # 创建label，创建之初指定父亲
#     btn2 = QPushButton("端口扫描", win2)
#     # 显示位置与大小：(x, y, w, h)
#     btn2.setGeometry(20, 200, 150, 80)
#     btn3 = QPushButton("系统检测", win2)
#     btn3.setGeometry(20, 300, 150, 80)
#     btn4 = QPushButton("爬取网页信息", win2)
#     btn4.setGeometry(300, 20, 150, 80)
#     btn5 = QPushButton("退出系统", win2)
#     btn5.setGeometry(300, 200, 150, 80)
#     # win2.show()
    
#     # 创建label，创建之初指定父亲
#     label = QLabel("Account: ", win)
#     # 显示位置与大小：(x, y, w, h)
#     label.setGeometry(20, 20, 100, 30)
#     # 创建label，创建之初指定父亲
#     label = QLabel("Password: ", win)
#     # 显示位置与大小：(x, y, w, h)
#     label.setGeometry(20, 50, 100, 30)
 
#     # 创建文本框
#     edit1 = QLineEdit(win)
#     edit1.setPlaceholderText("请输入账号")
#     edit1.setGeometry(90, 25, 200, 20)
#     # 创建文本框
#     edit2 = QLineEdit(win)
#     edit2.setEchoMode(PyQt5.QtWidgets.QLineEdit.Password)
#     edit2.setPlaceholderText("请输入密码")
#     edit2.setGeometry(100, 55, 190, 20)
 
#     # 在窗口里面添加控件
#     btn = QPushButton("登录", win)
#     btn.setGeometry(120, 90, 70, 30)
    
#     btn.clicked.connect(win.close)
#     # btn.clicked.connect(clickButton)
#     btn.clicked.connect(win2.show)
    
#     btn1.clicked.connect(clickButton1)
    
#     win.show()
    
#     # 启动主循环，开始程序的运行
#     sys.exit(app.exec_())
    
    
    
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
# 获取起始终止IP地址间的所有IP
from plugins.Scan.os_scan import osdetect
from plugins.Scan.port_scan import ScanPort
import time

from lib.output import console
from ipaddress import ip_address

from plugins.Crawl.web_crawl import Crawl
from plugins.Scan.active_scan import ActiveCheck

def findIPs(start, end):
    start = ip_address(start)
    end = ip_address(end)
    result = []
    while start <= end:
        result.append(str(start))
        start += 1
    return result


class Ui_MainWindow(object):
	def __init__(self):
		# 主界面初始化
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		# 一级菜单栏初始化
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menu = QtWidgets.QMenu(self.menubar)
		self.menu_2 = QtWidgets.QMenu(self.menubar)
		self.menu_3 = QtWidgets.QMenu(self.menubar)
		self.menu_4 = QtWidgets.QMenu(self.menubar)
		# 二级菜单栏初始化
		self.actionRGB_histogram = QtWidgets.QAction(MainWindow)
        # self.actionDomain = QtWidgets.QAction(MainWindow)
		self.actionDomain = QtWidgets.QAction(MainWindow)        
		self.action = QtWidgets.QAction(MainWindow)
		self.actionDAISY = QtWidgets.QAction(MainWindow)
		self.actionEHD = QtWidgets.QAction(MainWindow)
		self.action_2 = QtWidgets.QAction(MainWindow)
		self.actionVGG = QtWidgets.QAction(MainWindow)
		self.actionResNet = QtWidgets.QAction(MainWindow)
		# 界面布局
		self.Layout = QVBoxLayout(self.centralwidget)  # 垂直布局
		# stackedWidget初始化
		self.stackedWidget = QStackedWidget()

	def setupUi(self, MainWindow):
		# 创建界面
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(1440, 773)
		self.centralwidget.setObjectName("centralwidget")
		MainWindow.setCentralWidget(self.centralwidget)
		# 一级菜单栏布置
		self.menubar.setGeometry(QtCore.QRect(0, 0, 1440, 24))
		self.menubar.setObjectName("menubar")
		self.menu.setObjectName("menu")
		self.menu_2.setObjectName("menu_2")
		self.menu_3.setObjectName("menu_3")
		self.menu_4.setObjectName("menu_4")
		MainWindow.setMenuBar(self.menubar)
		# 二级菜单栏布 置
		self.actionRGB_histogram.setObjectName("actionRGB_histogram")
		self.actionDomain.setObjectName("actionDomain")        
		self.action.setObjectName("action")
		self.actionDAISY.setObjectName("actionDAISY")
		self.actionEHD.setObjectName("actionEHD")
		self.action_2.setObjectName("action_2")
		self.actionVGG.setObjectName("actionVGG")
		self.actionResNet.setObjectName("actionResNet")
# 		self.actionClick1.setObjectName("actionClick1")
		self.menu.addAction(self.actionRGB_histogram)
		self.menu.addAction(self.actionDomain)        
		self.menu_2.addAction(self.action)
		self.menu_3.addAction(self.actionDAISY)
# 		self.menu_3.addAction(self.actionEHD)
# 		self.menu_3.addAction(self.action_2)
		self.menu_4.addAction(self.actionVGG)
# 		self.menu_4.addAction(self.actionResNet)
		self.menubar.addAction(self.menu.menuAction())
		self.menubar.addAction(self.menu_2.menuAction())
		self.menubar.addAction(self.menu_3.menuAction())
		self.menubar.addAction(self.menu_4.menuAction())

		# 布局添加stackedWidget控件
		self.Layout.addWidget(self.stackedWidget)

		# 设置主界面面板：
		self.form = QWidget()
		self.formLayout = QHBoxLayout(self.form)  # 水平布局
		self.label0 = QLabel()
		self.label0.setText("主界面！")
		self.label0.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
		self.label0.setAlignment(Qt.AlignCenter)
		self.label0.setFont(QFont("Roman times", 50, QFont.Bold))
		self.formLayout.addWidget(self.label0)  # 添加控件

		# 设置第1个面板：
		self.form1 = QWidget()
		self.formLayout1 = QHBoxLayout(self.form1)  # 水平布局
		self.label1 = QLabel()
		self.label1.setText("Color")
		self.label1.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
		self.label1.setAlignment(Qt.AlignCenter)
		self.label1.setFont(QFont("Roman times", 50, QFont.Bold))
		self.btn1 = QtWidgets.QPushButton("确认")
		self.btn1.setGeometry(120, 90, 70, 30)
		self.edit1 = QLineEdit()
		self.edit1.setPlaceholderText("请输入起始ip")
		self.edit1.setGeometry(90, 25, 200, 20)
        # 创建文本框
		self.edit2 = QLineEdit()
		self.edit2.setPlaceholderText("请输入终止ip")
		self.edit2.setGeometry(200, 55, 190, 20)
		self.formLayout1.addWidget(self.label1)  # 添加控件
		
		self.formLayout1.addWidget(self.edit1)  # 添加控件
		self.formLayout1.addWidget(self.edit2)  # 添加控件
		self.formLayout1.addWidget(self.btn1)  # 添加控件
		
        # 设置第2个面板：
		self.form2 = QWidget()
		self.formLayout2 = QHBoxLayout(self.form2)
		self.label2 = QLabel()
		self.label2.setText("Gabor")
		self.label2.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
		self.label2.setAlignment(Qt.AlignCenter)
		self.label2.setFont(QFont("Roman times", 50, QFont.Bold))
		self.formLayout2.addWidget(self.label2)
		# 设置第3个面板：
		self.form3 = QWidget()
		self.formLayout3 = QHBoxLayout(self.form3)
		self.label3 = QLabel()
		self.label3.setText("DAISY")
		self.label3.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
		self.label3.setAlignment(Qt.AlignCenter)
		self.label3.setFont(QFont("Roman times", 50, QFont.Bold))
		self.formLayout3.addWidget(self.label3)
        
		# 设置第4个面板：
		self.form4 = QWidget()
		self.formLayout4 = QHBoxLayout(self.form4)
		self.label4 = QLabel()
		self.label4.setText("EHD")
		self.label4.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
		self.label4.setAlignment(Qt.AlignCenter)
		self.label4.setFont(QFont("Roman times", 50, QFont.Bold))
		self.formLayout4.addWidget(self.label4)
		self.btn2 = QtWidgets.QPushButton("确认")
		self.btn2.setGeometry(120, 90, 70, 30)
		self.edit3 = QLineEdit()
		self.edit3.setPlaceholderText("请输入域名")
		self.edit3.setGeometry(90, 25, 200, 20)
		self.formLayout4.addWidget(self.edit3)  # 添加控件
		self.formLayout4.addWidget(self.btn2)  # 添加控件
        
		# 设置第5个面板：
		self.form5 = QWidget()
		self.formLayout5 = QHBoxLayout(self.form5)
		self.label5 = QLabel()
		self.label5.setText("HOG")
		self.label5.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
		self.label5.setAlignment(Qt.AlignCenter)
		self.label5.setFont(QFont("Roman times", 50, QFont.Bold))
		self.formLayout5.addWidget(self.label5)
		# 设置第6个面板：
		self.form6 = QWidget()
		self.formLayout6 = QHBoxLayout(self.form6)
		self.label6 = QLabel()
		self.label6.setText("VGG")
		self.label6.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
		self.label6.setAlignment(Qt.AlignCenter)
		self.label6.setFont(QFont("Roman times", 50, QFont.Bold))
		self.formLayout6.addWidget(self.label6)
		# 设置第7个面板：
		self.form7 = QWidget()
		self.formLayout7 = QHBoxLayout(self.form7)
		self.label7 = QLabel()
		self.label7.setText("ResNet")
		self.label7.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
		self.label7.setAlignment(Qt.AlignCenter)
		self.label7.setFont(QFont("Roman times", 50, QFont.Bold))
		self.formLayout7.addWidget(self.label7)

		# stackedWidget添加各种界面用于菜单切换
		self.stackedWidget.addWidget(self.form)
		self.stackedWidget.addWidget(self.form1)
		self.stackedWidget.addWidget(self.form2)
		self.stackedWidget.addWidget(self.form3)
		self.stackedWidget.addWidget(self.form4)
		self.stackedWidget.addWidget(self.form5)
		self.stackedWidget.addWidget(self.form6)
		self.stackedWidget.addWidget(self.form7)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)


	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		# 窗口名称
		MainWindow.setWindowTitle(_translate("MainWindow", "欢迎进入系统"))
		# 一级目录
		self.menu.setTitle(_translate("MainWindow", "主机存活扫描"))
		self.menu_2.setTitle(_translate("MainWindow", "端口扫描"))
		self.menu_3.setTitle(_translate("MainWindow", "系统检测"))
		self.menu_4.setTitle(_translate("MainWindow", "爬取网页信息"))
		# 二级目录
		# Color方法1：RGB直方图
		self.actionRGB_histogram.setText(_translate("MainWindow", "ip扫描"))
		self.actionRGB_histogram.triggered.connect(self.gotoColorWin)
        
		self.actionDomain.setText(_translate("MainWindow", "域名扫描"))
		self.actionDomain.triggered.connect(self.gotoEHDWin)        
		# Texture方法1：Gabor滤波
		self.action.setText(_translate("MainWindow", "扫描端口"))
		self.action.triggered.connect(self.gotoTexWin)
        
		self.btn1.clicked.connect(self.gotoClick1)
        
		# shape方法1：DAISY算子
		self.actionDAISY.setText(_translate("MainWindow", "检测地址"))
		self.actionDAISY.triggered.connect(self.gotoDaisyWin)
		# shape方法2：EHD
		self.actionEHD.setText(_translate("MainWindow", "边缘直方图描述符（EHD）"))
		self.actionEHD.triggered.connect(self.gotoEHDWin)
		# shape方法3：HOG
		self.action_2.setText(_translate("MainWindow", "方向梯度直方图（HOG）"))
		self.action_2.triggered.connect(self.gotoHOGWin)
		# deep-learning方法1：VGG
		self.actionVGG.setText(_translate("MainWindow", "爬取地址"))
		self.actionVGG.triggered.connect(self.gotoVGGWin)
		# deep-learning方法2：ResNet
		self.actionResNet.setText(_translate("MainWindow", "ResNet"))
		self.actionResNet.triggered.connect(self.gotoResWin)

	# 菜单栏触发每个界面调用函数
	def gotoColorWin(self):
		self.stackedWidget.setCurrentIndex(1)
	def gotoTexWin(self):
		self.stackedWidget.setCurrentIndex(2)
	def gotoDaisyWin(self):
		self.stackedWidget.setCurrentIndex(3)
	def gotoEHDWin(self):
		self.stackedWidget.setCurrentIndex(4)
	def gotoHOGWin(self):
		self.stackedWidget.setCurrentIndex(5)
	def gotoVGGWin(self):
		self.stackedWidget.setCurrentIndex(6)
	def gotoResWin(self):
		self.stackedWidget.setCurrentIndex(7)
	def gotoClick1(self):
		start_ip = self.edit1.text()
		end_ip = self.edit2.text()
		start_time = time.time()
		active_hosts = ActiveCheck(findIPs(start_ip, end_ip), 'active_result').pool()
		end_time = time.time()
		self.label1.setText('\nrunning {0:.3f} seconds'.format(end_time - start_time))
		print('\nrunning {0:.3f} seconds'.format(end_time - start_time))
# 		print(start_ip)
        


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	win = QtWidgets.QMainWindow()
	win.setFixedSize(300,200)
        # 创建label，创建之初指定父亲
	label = QLabel("Account: ", win)
        # 显示位置与大小：(x, y, w, h)
	label.setGeometry(20, 20, 100, 30)
        # 创建label，创建之初指定父亲
	label = QLabel("Password: ", win)
        # 显示位置与大小：(x, y, w, h)
	label.setGeometry(20, 50, 100, 30)
    # 在窗口里面添加控件
	btn = QtWidgets.QPushButton("登录", win)
	btn.setGeometry(120, 90, 70, 30)
        # 创建文本框
	edit1 = QLineEdit(win)
	edit1.setPlaceholderText("请输入账号")
	edit1.setGeometry(90, 25, 200, 20)
        # 创建文本框
	edit2 = QLineEdit(win)
	edit2.setEchoMode(QtWidgets.QLineEdit.Password)
	edit2.setPlaceholderText("请输入密码")
	edit2.setGeometry(100, 55, 190, 20)
        
    # 设置窗口的标题栏
	win.setWindowTitle('登录')
	win.show()
    
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	btn.clicked.connect(win.close)
    # btn.clicked.connect(clickButton)
	btn.clicked.connect(MainWindow.show)
# 	MainWindow.show()
	sys.exit(app.exec_())
    
    

