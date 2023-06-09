# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 18:56:56 2023

@author: lenovo
"""
import time
import threading
from lib.output import console
from ipaddress import ip_address

from plugins.Crawl.web_crawl import Crawl
from plugins.Scan.active_scan import ActiveCheck


# 获取起始终止IP地址间的所有IP
from plugins.Scan.os_scan import osdetect
from plugins.Scan.port_scan import ScanPort
from time import sleep
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import sys
import qtawesome
from PyQt5.QtCore import QObject, pyqtSignal, QEventLoop, QTimer, QThread, QTime
from PyQt5.QtGui import QTextCursor, QFont
from PyQt5.QtWidgets import QTextEdit, QWidget, QHBoxLayout, QLabel, QSizePolicy, QLineEdit, QStackedWidget
from lib.output import console
class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.th = MyThread()
        self.th.signalForText.connect(self.onUpdateText)
        sys.stdout = self.th

    def onUpdateText(self,text):
        cursor = self.process.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(text)
        self.process.setTextCursor(cursor)
        self.process.ensureCursorVisible()

    def init_ui(self):
        self.setFixedSize(1000, 500)
        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局

        self.widget = QtWidgets.QWidget()  
        self.widget.setObjectName('widget')
        self.layout = QtWidgets.QGridLayout()
        self.widget.setLayout(self.layout)  # 设置部件布局为网格
        
        #一级目录
        self.menubar = QtWidgets.QMenuBar(self.main_widget)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 100, 20))
        self.menubar.setObjectName("menubar")
        self.layout.addWidget(self.menubar, 0, 0, 1, 4)
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu.setTitle("主机存活扫描")
        self.menu_2.setTitle("端口扫描")
        self.menu_3.setTitle("系统检测")
        self.menu_4.setTitle("爬取网页信息")
        #二级目录
        self.action1 = QtWidgets.QAction(self.main_widget)
        self.action2 = QtWidgets.QAction(self.main_widget)
        self.action3 = QtWidgets.QAction(self.main_widget)
        self.action4 = QtWidgets.QAction(self.main_widget)
        self.action5 = QtWidgets.QAction(self.main_widget)
        self.action6 = QtWidgets.QAction(self.main_widget)
        self.action1.setObjectName("action1")
        self.action2.setObjectName("action2")
        self.action3.setObjectName("action3")
        self.action4.setObjectName("action4")
        self.action5.setObjectName("action5")
        self.action6.setObjectName("action6")
        self.action1.setText("ip扫描")
        self.action2.setText("域名扫描")
        self.action3.setText("扫描端口")
        self.action4.setText("检测地址")
        self.action5.setText("爬取地址")
        self.menu.addAction(self.action1)
        self.menu.addAction(self.action2) 
        self.menu_2.addAction(self.action3)
        self.menu_3.addAction(self.action4)
        self.menu_4.addAction(self.action5)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.stackedWidget = QStackedWidget()

        # 创建第一个面板
        self.form1 = QtWidgets.QWidget()
        self.formLayout1 = QtWidgets.QGridLayout()  # 水平布局
        self.form1.setLayout(self.formLayout1)
        self.label1 = QLabel()
        self.label1.setText("start ip:")
        self.formLayout1.addWidget(self.label1, 1, 0, 1, 1)
        self.input1 = QtWidgets.QLineEdit()
        self.formLayout1.addWidget(self.input1, 1, 1, 1, 1)
        self.label2 = QLabel()
        self.label2.setText("end ip:")
        self.formLayout1.addWidget(self.label2, 1, 2, 1, 1)
        self.input2 = QtWidgets.QLineEdit()
        self.formLayout1.addWidget(self.input2, 1, 3, 1, 1)
        self.conform1 = QtWidgets.QPushButton("确认")
        self.formLayout1.addWidget(self.conform1, 1, 4, 1, 1)
        self.action1.triggered.connect(self.gotoAction1)
        self.conform1.clicked.connect(self.genConformClicked1)

        # 创建第二个面板
        self.form2 = QtWidgets.QWidget()
        self.formLayout2 = QtWidgets.QGridLayout()  # 水平布局
        self.form2.setLayout(self.formLayout2)
        self.label3 = QLabel()
        self.label3.setText("请输入正确域名：")
        self.formLayout2.addWidget(self.label3, 1, 0, 1, 1)
        self.input3 = QtWidgets.QLineEdit()
        self.formLayout2.addWidget(self.input3, 1, 1, 1, 1)
        self.conform2 = QtWidgets.QPushButton("确认")
        self.formLayout2.addWidget(self.conform2, 1, 4, 1, 1)
        self.action2.triggered.connect(self.gotoAction2)
        self.conform2.clicked.connect(self.genConformClicked2)

        # 创建第三个面板
        self.form3 = QtWidgets.QWidget()
        self.formLayout3 = QtWidgets.QGridLayout()  # 水平布局
        self.form3.setLayout(self.formLayout3)
        self.label4 = QLabel()
        self.label4.setText("请输入正确端口：")
        self.formLayout3.addWidget(self.label4, 1, 0, 1, 1)
        self.input4 = QtWidgets.QLineEdit()
        self.formLayout3.addWidget(self.input4, 1, 1, 1, 1)
        self.conform3 = QtWidgets.QPushButton("确认")
        self.formLayout3.addWidget(self.conform3, 1, 4, 1, 1)
        self.action3.triggered.connect(self.gotoAction3)
        self.conform3.clicked.connect(self.genConformClicked3)

        # 创建第四个面板
        self.form4 = QtWidgets.QWidget()
        self.formLayout4 = QtWidgets.QGridLayout()  # 水平布局
        self.form4.setLayout(self.formLayout4)
        self.label5 = QLabel()
        self.label5.setText("请输入检测地址：")
        self.formLayout4.addWidget(self.label5, 1, 0, 1, 1)
        self.input5 = QtWidgets.QLineEdit()
        self.formLayout4.addWidget(self.input5, 1, 1, 1, 1)
        self.conform4 = QtWidgets.QPushButton("确认")
        self.formLayout4.addWidget(self.conform4, 1, 4, 1, 1)
        self.action4.triggered.connect(self.gotoAction4)
        self.conform4.clicked.connect(self.genConformClicked4)

        # 创建第五个面板
        self.form5 = QtWidgets.QWidget()
        self.formLayout5 = QtWidgets.QGridLayout()  # 水平布局
        self.form5.setLayout(self.formLayout5)
        self.label6 = QLabel()
        self.label6.setText("请输入爬取地址：")
        self.formLayout5.addWidget(self.label6, 1, 0, 1, 1)
        self.input6 = QtWidgets.QLineEdit()
        self.formLayout5.addWidget(self.input6, 1, 1, 1, 1)
        self.conform5 = QtWidgets.QPushButton("确认")
        self.formLayout5.addWidget(self.conform5, 1, 4, 1, 1)
        self.action5.triggered.connect(self.gotoAction5)
        self.conform5.clicked.connect(self.genConformClicked5)
        
        self.main_layout.addWidget(self.widget, 0, 2, 12, 10)  
        self.setCentralWidget(self.main_widget)  # 设置窗口主部件
        
        # self.bar_widget = QtWidgets.QWidget()  # 顶部搜索框部件
        # self.bar_layout = QtWidgets.QGridLayout()  # 顶部搜索框网格布局
        # self.bar_widget.setLayout(self.bar_layout)
        # self.search_button = QtWidgets.QPushButton(qtawesome.icon('fa.comment', color='red'), "搜索")
        # self.search_button.clicked.connect(self.genMastClicked)
        # self.search_button.setObjectName('button')
        # self.search_button.setFont(qtawesome.font('fa', 16))
        # self.bar_widget_search_input = QtWidgets.QLineEdit()  # 搜索框
        # self.bar_widget_search_input.setPlaceholderText("输入搜索内容")
        # self.conform_button = QtWidgets.QPushButton("确认")
        # self.conform_button.clicked.connect(self.genConformClicked)
        # self.conform_button.setObjectName('button1')

        # self.bar_layout.addWidget(self.search_button, 1, 0, 1, 1)
        # self.bar_layout.addWidget(self.bar_widget_search_input, 1, 1, 1, 7)
        # self.bar_layout.addWidget(self.conform_button, 1, 8, 1, 1)

        # self.layout.addWidget(self.bar_widget, 1, 0, 1, 9)
        self.layout.addWidget(self.stackedWidget, 1, 0, 1, 9) # 添加子界面

        self.recommend_label = QtWidgets.QLabel("进程显示：")
        self.recommend_label.setObjectName('lable')

        self.recommend_widget = QtWidgets.QWidget()
        self.recommend_layout = QtWidgets.QGridLayout()
        self.recommend_widget.setLayout(self.recommend_layout)

        self.process = QTextEdit(self, readOnly=True)
        self.process.ensureCursorVisible()
        self.process.setLineWrapColumnOrWidth(800)
        self.process.setLineWrapMode(QTextEdit.FixedPixelWidth)
        self.process.setFixedWidth(500)
        self.process.setFixedHeight(250)
        self.process.move(30, 50)

        self.recommend_layout.addWidget(self.process, 0, 1)
        self.layout.addWidget(self.recommend_label, 2, 0, 1, 9)
        self.layout.addWidget(self.recommend_widget, 2, 0, 2, 9)

        #使用QSS和部件属性美化窗口部件
        self.stackedWidget.setStyleSheet(
            '''QLineEdit{
                    border:1px solid gray;
                    width:10px;
                    border-radius:10px;
                    padding:2px 4px;
            }''')
        self.widget.setStyleSheet('''
            QWidget#widget{
                color:#232C51;
                background:white;
                border-top:1px solid darkGray;
                border-bottom:1px solid darkGray;
                border-right:1px solid darkGray;
            }
            QLabel#lable{
                border:none;
                font-size:16px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
            QPushButton#button:hover{border-left:4px solid red;font-weight:700;}
        ''')

    # 清空子界面的组件
    def clearStack(self):
        self.stackedWidget.removeWidget(self.form1)
        self.stackedWidget.removeWidget(self.form2)
        self.stackedWidget.removeWidget(self.form3)
        self.stackedWidget.removeWidget(self.form4)
        self.stackedWidget.removeWidget(self.form5)
        # for x in self.stackedWidget:
        #     self.stackedWidget.removeWidget(x)

    # 菜单栏触发每个界面调用函数
    def gotoAction1(self):
        self.clearStack()
        self.stackedWidget.addWidget(self.form1)
        # self.stackedWidget.setCurrentIndex(1)

    def gotoAction2(self):
        self.clearStack()
        self.stackedWidget.addWidget(self.form2)
        # self.stackedWidget.setCurrentIndex(2)

    def gotoAction3(self):
        self.clearStack()
        self.stackedWidget.addWidget(self.form3)
        # self.stackedWidget.setCurrentIndex(3)

    def gotoAction4(self):
        self.clearStack()
        self.stackedWidget.addWidget(self.form4)
        # self.stackedWidget.setCurrentIndex(4)

    def gotoAction5(self):
        self.clearStack()
        self.stackedWidget.addWidget(self.form5)
        # self.stackedWidget.setCurrentIndex(5)

    def gotoAction6(self):
        self.stackedWidget.setCurrentIndex(6)

    def gotoResWin(self):
        self.stackedWidget.setCurrentIndex(7)

    def search(self):
        try:
            self.t = MyThread()
            self.t.start()
        except Exception as e:
            raise e

    def genMastClicked(self):
        """Runs the main function."""
        print('Running...')
        if self.conform_button.isChecked() == True:
            print("sucsess")
        self.search()

        loop = QEventLoop()
        QTimer.singleShot(2000, loop.quit)
        loop.exec_()

    def thread_func(self, string): 
        print(string) 
        time.sleep(5)
            
    def genConformClicked1(self):
        startip = self.input1.text()
        endip = self.input2.text()
        start_time = time.time()
        active_hosts = ActiveCheck(findIPs(startip, endip), 'active_result').pool()
        end_time = time.time()
        print('\nrunning {0:.3f} seconds'.format(end_time - start_time))

    def genConformClicked2(self):
        domain = self.input3.text()
        start_time = time.time()
        active_hosts = ActiveCheck(domain, 'active_result').pool()
        end_time = time.time()
        print('\nrunning {0:.3f} seconds'.format(end_time - start_time))

    def genConformClicked3(self):
        port = self.input4.text()
        start_time = time.time()
        ScanPort(port, 'port_result').pool()
        end_time = time.time()
        print('\nrunning {0:.3f} seconds'.format(end_time - start_time))

    def genConformClicked4(self):
        port = self.input5.text()
        start_time = time.time()
        osdetect(port, 'os_result')
        end_time = time.time()
        print('\nrunning {0:.3f} seconds'.format(end_time - start_time))

    def genConformClicked5(self):
        ip = self.input6.text()
        print(ip)
        
    def closeEvent(self, event):
        """Shuts down application on close."""
        # Return stdout to defaults.
        sys.stdout = sys.__stdout__
        super().closeEvent(event)

class MyThread(QThread):
    signalForText = pyqtSignal(str)

    def __init__(self,data=None, parent=None):
        super(MyThread, self).__init__(parent)
        self.data = data

    def write(self, text):
        self.signalForText.emit(str(text))  # 发射信号

    def run(self):
        while 1:
            print('欢迎使用扫描系统!', '请选择功能 ', "1.主机存活扫描  2.端口扫描  3.系统检测  4.爬取网页信息 5.退出系统"+'\n')
            choose = 1
            if choose == '1':
                print('请选择扫描IP地址或者域名！', '请选择功能 ', '1.IP地址  2.域名'+'\n')
                choose1=self.bar_widget_search_input.text()
                if choose1 == '1':
                    start_ip = input('使用主机存活扫描，请输入起始IP地址：')
                    end_ip = input('请输入终止IP地址：')
                    start_time = time.time()
                    active_hosts = ActiveCheck(findIPs(start_ip, end_ip), 'active_result').pool()
                    end_time = time.time()
                    print('\nrunning {0:.3f} seconds'.format(end_time - start_time))
                elif choose1 == '2':
                    d = []
                    d.append(input('使用主机存活扫描，请输入扫描域名'))
                    start_time = time.time()
                    active_hosts = ActiveCheck(d, 'active_result').pool()
                    end_time = time.time()
                    print('\nrunning {0:.3f} seconds'.format(end_time - start_time))
            elif choose == '2':
                p = input('使用端口扫描，请输入扫描地址：')
                start_time = time.time()
                ScanPort(p, 'port_result').pool()
                end_time = time.time()
                print('\nrunning {0:.3f} seconds...'.format(end_time - start_time))
            elif choose == '3':
                p = input('使用系统检测，请输入检测地址：')
                start_time = time.time()
                osdetect(p, 'os_result')
                end_time = time.time()
                print('\nrunning {0:.3f} seconds'.format(end_time - start_time))
            elif choose == '4':
                w = input('使用网页信息爬取，请输入爬取地址：')
                start_time = time.time()
                Crawl(w, 'crawl_result').pool()
                end_time = time.time()
                print('\nrunning {0:.3f} seconds'.format(end_time - start_time))
            elif choose == '5':
                exit(0)
            else:
                print('请重新输入正确的选项！')
    
    
    
def findIPs(start, end):
    start = ip_address(start)
    end = ip_address(end)
    result = []
    while start <= end:
        result.append(str(start))
        start += 1
    return result

def main():
    app = QtWidgets.QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    gui = MainUi()
    gui.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
