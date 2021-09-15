# 从selenium导入webdriver
from selenium import webdriver
#导入异常
from selenium.common import exceptions as ex
import time


# def set_page(driver):
#     #获取一百页格式的元素
#     page_style = driver.find_elements_by_class_name('Select_option__k61AN')
#     page_style[2].click()
#     page_style = driver.find_elements_by_class_name('Select_option__k61AN')
#
#     print(page_style[7].text)
#     page_style[7].click()
#     time.sleep(1)



def set_page(driver):
    time.sleep(5)
    #获取一百页格式的元素
    page_style = driver.find_element_by_class_name('Select_select__TBmtu')
    page_style.click()
    page_style = driver.find_elements_by_class_name('Select_option__k61AN')
    print(page_style[4].text)
    page_style[4].click()
    time.sleep(1)


if __name__ == '__main__':
    url = "https://explorer.btc.com/btc/transactions"
    # 声明调用哪个浏览器，本文使用的是Chrome，其他浏览器同理。有如下两种方法及适用情况
    driver = webdriver.Chrome()  # 把Chromedriver放到python安装路径里

    driver.get(url=url)
    set_page(driver)