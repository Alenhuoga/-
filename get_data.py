# 从selenium导入webdriver
from selenium import webdriver
import csv
import os




# # 声明调用哪个浏览器，本文使用的是Chrome，其他浏览器同理。有如下两种方法及适用情况
# driver = webdriver.Chrome()  # 把Chromedriver放到python安装路径里

# #不开浏览器
# # 不开网页搜索
# option = webdriver.ChromeOptions()
# option.add_argument("headless")
#
#
# #设置后台静默模式启动浏览器
# option.add_argument("--no-sandbox");
# option.add_argument("--disable-dev-shm-usage");
#
# driver = webdriver.Chrome(chrome_options=option)
def get_data(url,driver):

    row = []


    driver.get(url=url)

    #交易哈希
    hash_num = driver.find_elements_by_class_name('TopSummary_content__39aee')

    #1.hash
    row.append(hash_num[0].text)


    print(hash_num[0].text)

    #找到区块
    block_data = driver.find_elements_by_class_name('justify-between')

    #区块内所有信息
    for i in range(len(block_data)):
        #剔除体积
        if i !=3:
            a = block_data[i].text
            #分割
            print(a.splitlines())
            print('*****')
            row.append(a.splitlines()[1])



    #底部输入输出框 列表 第一个位置表输入 第二个表输出
    block_bottom = driver.find_elements_by_class_name('TxListItem_list-items__2Ganp')

    input_arr = block_bottom[0].find_elements_by_class_name('monospace')

    input_add = ''
    for i in input_arr:
        input_add = input_add + i.text + ','

    print(input_add)
    row.append(input_add)

    out_arr = block_bottom[1].find_elements_by_class_name('monospace')
    out_add = ''
    for i in out_arr:
        out_add = out_add + i.text + ','

    print(out_add)
    row.append(out_add)
    print(row)

    # driver.close()
    return row


if __name__ == '__main__':
    url = "https://explorer.btc.com/btc/transaction/548488e5416457b2045925430b14828aa0a3228cb266f452709ebfc13a7a7def"

    # 声明调用哪个浏览器，本文使用的是Chrome，其他浏览器同理。有如下两种方法及适用情况
    driver = webdriver.Chrome()  # 把Chromedriver放到python安装路径里

    #不开浏览器
    # 不开网页搜索
    option = webdriver.ChromeOptions()
    option.add_argument("headless")


    #设置后台静默模式启动浏览器
    option.add_argument("--no-sandbox");
    option.add_argument("--disable-dev-shm-usage");

    driver = webdriver.Chrome(chrome_options=option)
    get_data(url,driver)
