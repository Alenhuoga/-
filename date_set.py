# 从selenium导入webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys   #引用keys包
import time


# def date_set(from_time,to_time,driver):
#     input_from = driver.find_element_by_xpath('//*[@id="__next"]/div[2]/div[2]/div[2]/div[1]/div/div[1]/input')
#     input_to =driver.find_element_by_xpath('//*[@id="__next"]/div[2]/div[2]/div[2]/div[1]/div/div[3]/input')
#
#     input_from.send_keys(from_time)
#     input_to.send_keys(to_time)
#     time.sleep(1)
#     input_to.send_keys(Keys.ENTER)
#     time.sleep(1)

def date_set(from_time,to_time,driver):
    input_from = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div[2]/div[1]/div/div/div/div[1]/input')
    input_to =driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div[2]/div[1]/div/div/div/div[3]/input')

    input_from.send_keys(from_time)
    input_to.send_keys(to_time)
    time.sleep(1)
    input_to.send_keys(Keys.ENTER)
    time.sleep(1)


if __name__ == '__main__':

    url = "https://explorer.btc.com/btc/transactions"
    driver = webdriver.Chrome()  # 把Chromedriver放到python安装路径里

    driver.get(url=url)
    from_time = '2009-01-10'
    to_time = '2010-01-10'
    date_set(from_time,to_time,driver)