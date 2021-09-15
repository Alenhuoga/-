import pandas as pd
from tqdm import tqdm
import os


import re


#构造跨表合并的函数
def Cross_table(path):
    df_list = []
    for file in tqdm(os.listdir(path)):##进度条

        print(file)
        file_path = os.path.join(path, file)
        df = pd.read_csv(file_path,encoding = 'GB18030')
        print(df)
        df_list.append(df)

    print(df_list)
    df = pd.concat(df_list)
    return df

#构造跨表合并的函数
def Cross_table_host(path):
    df_list = []

    pattern = r".csv"
    print(os.listdir(path))
    for file in tqdm(os.listdir(path)):##进度条

        print(file)
        print(re.search(pattern, file))
        if re.search(pattern,file) != None:
            file_path = os.path.join(path, file)
            df = pd.read_csv(file_path,encoding = 'GB18030')
            print(df)
            df_list.append(df)
    print(df_list)
    df = pd.concat(df_list)
    return df

#构造跨表合并的函数
def Cross_table_all(path):
    df_list = []

    pattern = r"total"
    print(os.listdir(path))
    for file in tqdm(os.listdir(path)):##进度条

        print(file)
        print(re.search(pattern, file))
        if re.search(pattern,file) != None:
            file_path = os.path.join(path, file)
            df = pd.read_csv(file_path)
            print(df)
            df_list.append(df)
    print(df_list)
    df = pd.concat(df_list)
    return df

# #传入地址并执行结果
# ServerData_PATH = 'F:\研一\crawler_for_btc'
# #生成合并后的数据表
# ServerData_df = Cross_table(ServerData_PATH)
#
# ServerData_df.to_csv("F:\研一\crawler_for_btc\\total1.csv")
#本机数据位置
# HostData_PATH = 'F:\大四\\btc_web_crawler'
#
#
#
# HostData_df = Cross_table_host(HostData_PATH)
#
#
# HostData_df.to_csv("F:\研一\crawler_for_btc\\total2.csv")

#生成总表
Data_PATH = 'F:\研一\crawler_for_btc'
Data_df=Cross_table_all(Data_PATH)
Data_df.to_csv("F:\研一\crawler_for_btc\\total.csv")