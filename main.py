# 从selenium导入webdriver
from selenium import webdriver
import time
from get_data import get_data
import os
from date_set import date_set
import csv
import time
from page_style import set_page
import pandas as pd
import multiprocessing
from parameter import set_args

#导入异常
from selenium.common import exceptions as ex
import _thread
import time, threading

#翻页
def next_page():
    li = driver.find_elements_by_class_name('Pagination_root__24U4V')
    for i in range(len(li)):
        li = driver.find_elements_by_class_name('Pagination_root__24U4V')
        if li[i].find_elements_by_class_name('Pagination_active__wo_1Z'):
            a = li[i + 1].find_elements_by_class_name('Pagination_button__3YHHq')
            print(a[0].text)

            df.to_csv("page.txt",index=False)
            df["t1"][0] = a[0].text
            a[0].click()

            # time.sleep(4)
            # print(a[0].text)
            break

#用于恢复断点页面
def page_recover(page_index):
    # 恢复多少页
    for i in range(page_index):
        li = driver.find_elements_by_class_name('Pagination_root__24U4V')
        for i in range(len(li)):
            li = driver.find_elements_by_class_name('Pagination_root__24U4V')
            #找到当前定位的页面
            if li[i].find_elements_by_class_name('Pagination_active__wo_1Z'):
                if int(li[i].find_elements_by_class_name('Pagination_active__wo_1Z')[0].text)>=4 and (int(li[i].find_elements_by_class_name('Pagination_active__wo_1Z')[0].text)+5)<=page_index:
                    a1 = li[i + 2].find_elements_by_class_name('Pagination_button__3YHHq')
                    print(li[i].find_elements_by_class_name('Pagination_active__wo_1Z')[0].text)
                    a1[0].click()
                    break
                elif int(li[i].find_elements_by_class_name('Pagination_active__wo_1Z')[0].text)<=page_index:
                    #当个页的下一页
                    a = li[i + 1].find_elements_by_class_name('Pagination_button__3YHHq')
                    print(a[0].text)
                    a[0].click()

                    # time.sleep(4)
                    # print(a[0].text)
                    break


#参数
args = set_args()

url = "https://explorer.btc.com/btc/transactions"

#没有弹窗模式
options = webdriver.ChromeOptions()
# #静默模式打开,不打开浏览器
# options.add_argument('--headless')

options.add_argument('--no-sandbox')
# 不加载图片, 提升速度
options.add_argument('blink-settings=imagesEnabled=false')

# 谷歌文档提到需要加上这个属性来规避bug
options.add_argument('--disable-gpu')

# 禁用JavaScript
options.add_argument("--disable-javascript")

driver = webdriver.Chrome(chrome_options=options)

# 弹窗模式
# driver = webdriver.Chrome()  # 把Chromedriver放到python安装路径里

# driver.get(url=url)


#不开浏览器
# 不开网页搜索
data_option = webdriver.ChromeOptions()
data_option.add_argument("headless")


#设置后台静默模式启动浏览器
data_option.add_argument("--no-sandbox");
data_option.add_argument("--disable-dev-shm-usage");

driver_data = webdriver.Chrome(chrome_options=data_option)


size = os.path.getsize('page.txt')
#判断文件是否初始为空
if size == 0:

    print('文件是空的')
    # 用于保存断点
    page = {"t1": [0], "t2": [0], "t3": [0], "t4": [0], "t5": [0],"t6": [0], "t7": [0], "t8": [0], "t9": [0], "t10": [0]}
    # 全局化一个df对象
    df = pd.DataFrame(page)
    df.to_csv("page.txt", index=False)
else:
    print('文件不是空的')
    df = pd.read_csv('page.txt')

print(df)

# 爬取的时间段
from_time = '2010-01-10'
to_time = '2020-01-10'

# 文件写在当前路径下
path = {'path1':os.path.abspath('.') + '\\btc1.csv','path2':os.path.abspath('.') + '\\btc2.csv',
        'path3':os.path.abspath('.') + '\\btc3.csv','path4':os.path.abspath('.') + '\\btc4.csv',
        'path5':os.path.abspath('.') + '\\btc5.csv','path6':os.path.abspath('.') + '\\btc6.csv',
        'path7':os.path.abspath('.') + '\\btc7.csv','path8':os.path.abspath('.') + '\\btc8.csv',
        'path9':os.path.abspath('.') + '\\btc9.csv','path10':os.path.abspath('.') + '\\btc10.csv',}


def t_crawler(path,from_time,to_time,t_number):
    # 声明调用哪个浏览器，本文使用的是Chrome，其他浏览器同理。有如下两种方法及适用情况


    driver.get(url=url)
    time.sleep(3)

    #获取一百页格式的元素
    set_page(driver)

    # 设置爬取时间段
    date_set(from_time, to_time, driver)

    #获取一百页格式的元素
    set_page(driver)
    #

    #获取恢复断点页
    page_index = df[t_number][0]

    # 恢复断点页
    page_recover(page_index)

    with open(path, 'a+',newline='') as f:
        csv_writer = csv.writer(f)

        size = os.path.getsize(path)

        # 判断文件是否初始为空
        if size == 0:

            print('文件是空的')
            csv_writer.writerow(
                ['交易哈希', '区块高度', '确认数', '确认时间', '虚拟交易大小', 'Weight', '状态', '输入', '输出', 'Sigops', '手续费', '矿工费率(BTC/kVB)',
                 '输入地址', '输出地址'])
        else:
            print('文件不是空的')



        # total_bach = 0

        #爬取多少页
        for i in range(args.pages):

            while True:
                try:
                    element = driver.find_elements_by_class_name('monospace')
                    print(element)

                    #一页100条数据 爬取 num_of_page条
                    for i in range(args.num_of_page):


                        # total_bach = total_bach + 1

                        print(element[i].get_property(name="href"))

                        csv_writer.writerow(get_data(element[i].get_property(name="href"),driver_data))

                    # 翻下一页
                    li = driver.find_elements_by_class_name('Pagination_root__24U4V')
                    for i in range(len(li)):
                        if li[i].find_elements_by_class_name('Pagination_active__wo_1Z'):
                            a = li[i + 1].find_elements_by_class_name('Pagination_button__3YHHq')
                            a[0].click()
                            # 获取当前页码的页号，后续翻页
                            a[0].text

                            #保存当前页
                            df[t_number] = a[0].text
                            df.to_csv("page.txt", index=False)
                            time.sleep(4)
                            # print(a[0].text)
                            break
                    break
                except ex.StaleElementReferenceException:
                    print('抛出异常StaleElementReferenceException')
                    time.sleep(4)

                    #翻五页
                    for i in range(2):
                        li = driver.find_elements_by_class_name('Pagination_root__24U4V')
                        for i in range(len(li)):
                            if li[i].find_elements_by_class_name('Pagination_active__wo_1Z'):
                                a = li[i + 1].find_elements_by_class_name('Pagination_button__3YHHq')
                                a[0].click()
                                time.sleep(4)
                                # print(a[0].text)
                                break
                except IndexError:
                    print('抛出异常IndexError')
                    time.sleep(4)

                    #翻五页
                    for i in range(2):
                        li = driver.find_elements_by_class_name('Pagination_root__24U4V')
                        for i in range(len(li)):
                            if li[i].find_elements_by_class_name('Pagination_active__wo_1Z'):
                                a = li[i + 1].find_elements_by_class_name('Pagination_button__3YHHq')
                                a[0].click()
                                time.sleep(4)
                                # print(a[0].text)
                                break
                except ex.WebDriverException:
                    print('抛出异常WebDriverException')
                    time.sleep(4)
                    # 翻五页
                    time.sleep(4)

                    # 翻五页
                    for i in range(2):
                        li = driver.find_elements_by_class_name('Pagination_root__24U4V')
                        for i in range(len(li)):
                            if li[i].find_elements_by_class_name('Pagination_active__wo_1Z'):
                                a = li[i + 1].find_elements_by_class_name('Pagination_button__3YHHq')
                                a[0].click()
                                time.sleep(4)
                                # print(a[0].text)
                                break



if __name__ == '__main__':
    if args.year == '2010to2011':
        t_crawler(path=path['path1'],from_time='2010-01-11',to_time='2011-01-08',t_number="t1")
    if args.year == '2011to2012':
        t_crawler(path=path['path2'], from_time='2011-01-11', to_time='2011-12-27', t_number="t2")

    if args.year == '2012to2013':
        t_crawler(path=path['path3'],from_time='2012-01-11',to_time='2013-01-06',t_number="t3")
    if args.year == '2013to2014':
        t_crawler(path=path['path4'], from_time='2013-01-11', to_time='2014-01-08', t_number="t4")

    if args.year == '2014to2015':
        t_crawler(path=path['path5'],from_time='2014-01-11',to_time='2015-01-09',t_number="t5")
    if args.year == '2015to2016':
        t_crawler(path=path['path6'], from_time='2015-01-11', to_time='2016-01-09', t_number="t6")

    if args.year == '2016to2017':
        t_crawler(path=path['path7'],from_time='2016-01-11',to_time='2017-01-09',t_number="t7")
    if args.year == '2017to2018':
        t_crawler(path=path['path8'], from_time='2017-01-11', to_time='2018-01-09', t_number="t8")

    if args.year == '2018to2019':
        t_crawler(path=path['path9'], from_time='2018-01-11', to_time='2019-01-09', t_number="t9")
    if args.year == '2019to2020':
        t_crawler(path=path['path10'], from_time='2019-01-11', to_time='2020-01-09', t_number="t10")
