# -*- coding: utf-8 -*-
from mysql_handler import MysqlHandler
from html_downloader import HtmlDownloader
from html_parser import HtmlParser
import traceback
import time


class CodeSpider(object):
    def __init__(self):
        # 实例化其他模块类
        self.mysql_handler = MysqlHandler()
        self.html_downloader = HtmlDownloader()
        self.html_parser = HtmlParser()
        # 爬取起点url
        # self.root_url = 'http://infomap.cdedu.gov.cn/Home/Index?all=1&pages=1'
        # # 用于后续url的拼接
        # self.split_url = 'http://infomap.cdedu.gov.cn/Home/Index?all=1&pages='
        # # school info
        # self.school_infos = []
        #日志文件路径需要自行修改
        # self.last_log_path = "d:\\log.txt"
        # self.last_log_path = "/Users/spike/spider_log.txt"
    def craw(self,downloading_url):
        try:
            # 记录正在下载、解析的url，便于分析错误
            # downloading_url = self.root_url
            html_content = self.html_downloader.download(downloading_url)
            # 第一个参数：需要解析的html代码
            self.school_infos = self.html_parser.province_parser(html_content)
            # print(self.school_infos)
            if (len(self.school_infos)!=20):
                print(downloading_url+"解析成功")
                print("当前页面数据："+str(len(self.school_infos)))
            for mc,xd,qy,xz,dh,dz in self.school_infos:
                # print(mc+xd+qy+xz+dh+dz)
                province_id = self.mysql_handler.insert(mc,xd,qy,xz,dh,dz)     
                # print(province_id)
                # exit()
                # 记录正在下载、解析的url，便于分析错误  
            # self.mysql_handler.close()
            return len(self.school_infos)
        except Exception as e:
            print('[ERROR] Craw Field!Url:', downloading_url, 'Info:', e)
            # 利用traceback定位异常
            traceback.print_exc()
            time.sleep(60)            
            # return self.craw()

if __name__ == '__main__':
    obj_spider = CodeSpider()
    split_url = 'http://infomap.cdedu.gov.cn/Home/Index?all=1&pages='
    #一共123页数据
    sum=0
    for i in range(1,124):
        # print(i)
        sum=sum+obj_spider.craw(split_url+str(i))
        print("第"+str(i)+"页搞定")
    print("成功爬取"+str(sum)+"条数据")
