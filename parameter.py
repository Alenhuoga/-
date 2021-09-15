import argparse

def set_args():
    parser = argparse.ArgumentParser(description='爬虫代码参数')

    parser.add_argument("--year",default='2010',type=str,help='--year')
    #一页爬取多少条数据
    parser.add_argument("--num_of_page",type=int,default=100,help='--num_of_page')

    #爬取多少页
    parser.add_argument("--pages",type=int,default=4000,help='--pages')
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = set_args()

    print(args.year)
