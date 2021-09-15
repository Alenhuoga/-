js1 = 'var buttons = document.getElementsByTagName("button");'
# 从selenium导入webdriver
from selenium import webdriver
import time
import pandas as pd
url = "https://explorer.btc.com/btc/transactions"

# #没有弹窗模式
# options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
# driver = webdriver.Chrome(chrome_options=options)


# 弹窗模式
driver = webdriver.Chrome()  # 把Chromedriver放到python安装路径里

driver.get(url=url)
# b = driver.find_elements_by_class_name('Pagination_active__wo_1Z')
# print(b)
#用于保存断点
page={"t1":[0],"t2":[0],"t3":[0],"t4":[0],"t5":[0]}

def next_page():
    li = driver.find_elements_by_class_name('Pagination_root__24U4V')
    for i in range(len(li)):
        #找到当前页
        if li[i].find_elements_by_class_name('Pagination_active__wo_1Z'):
            #当个页的下一页
            a = li[i + 1].find_elements_by_class_name('Pagination_button__3YHHq')
            # a1 = li[i + 2].find_elements_by_class_name('Pagination_button__3YHHq')
            # print(a1[0].text)
            print(a[0].text)
            df = pd.DataFrame(page)
            df.to_csv("page1.txt",index=False)
            df["t1"][0] = a[0].text

            a[0].click()

            # time.sleep(4)
            # print(a[0].text)
            break


def page_recover(page_index):
    # 连翻25页
    for i in range(page_index):
        li = driver.find_elements_by_class_name('Pagination_root__24U4V')
        for i in range(len(li)):
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


if __name__ == '__main__':
    # for i in range(25):
    #     next_page()


    page_recover(25)


