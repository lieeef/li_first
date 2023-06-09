import time
from lib.output import console
from ipaddress import ip_address

from plugins.Crawl.web_crawl import Crawl
from plugins.Scan.active_scan import ActiveCheck
from threading import Thread  # 导入线程函数
from time import sleep  # 导入时间休眠函数

# 获取起始终止IP地址间的所有IP
from plugins.Scan.os_scan import osdetect
from plugins.Scan.port_scan import ScanPort
# from douban_flask.app import start
import douban_flask.app

def findIPs(start, end):
    start = ip_address(start)
    end = ip_address(end)
    result = []
    while start <= end:
        result.append(str(start))
        start += 1
    return result

def ExeStart():
    while 1:
        console('欢迎使用MiniScanner!', '请选择功能 ', "1.主机存活扫描  2.端口扫描  3.系统检测  4.爬取网页信息 5.爬取网页信息"+'\n')
        choose = input()
        time.sleep(5)
        print("yes")
        if choose == '1':
            console('请选择扫描IP地址或者域名！', '请选择功能 ', '1.IP地址  2.域名'+'\n')
            choose1=input()
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
            print("ok")
            # w = input('使用网页信息爬取，请输入爬取地址：')
            # start_time = time.time()
            # Crawl(w, 'crawl_result').pool()
            # end_time = time.time()
            # print('\nrunning {0:.3f} seconds'.format(end_time - start_time))
        elif choose == '5':
            exit(0)
        # elif choose == '6':
        #     douban_flask.app
        else:
            print('请重新输入正确的选项！')

if __name__ == "__main__":
        t1 = Thread(target=ExeStart)
        t2 = Thread(target=douban_flask.app.start)
        t1.start()
        t1.join()
        t2.start()
        # douban_flask.app.start()




