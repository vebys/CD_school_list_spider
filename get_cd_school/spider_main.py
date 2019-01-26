# -*- coding: utf-8 -*-
#from mysql_handler import MysqlHandler
from html_downloader import HtmlDownloader
from html_parser import HtmlParser
import traceback


class CodeSpider(object):
    def __init__(self):
        # 实例化其他模块类
        #self.mysql_handler = MysqlHandler()
        self.html_downloader = HtmlDownloader()
        self.html_parser = HtmlParser()
        self.path = "/Users/spike/python_项目/get_cd_school/"
        # # 爬取起点url
        # self.root_url = 'http://infomap.cdedu.gov.cn/Home/Index?all=1&pages=1'
        # # 用于后续url的拼接
        # self.split_url = 'http://infomap.cdedu.gov.cn/Home/Index?all=1&pages='
        # school info
        # self.school_infos = []
        

    def craw(self,downloading_url):
        try:
            # 记录正在下载、解析的url，便于分析错误
            # downloading_url = self.root_url
            html_content = self.html_downloader.download(downloading_url)
            # 第一个参数：需要解析的html代码
            # 第二个参数：用于url拼接的url
            self.school_infos = self.html_parser.province_parser(html_content)
            # print(self.school_infos)
            #exit()
            if (len(self.school_infos)!=20):
                print(downloading_url+"解析成功")
                print("当前页面数据："+str(len(self.school_infos)))
            #print(self.province_url_list)
            with open(self.path+"school.txt", "a") as f:
                # print("writting")
                for mc,xd,qy,xz,dh,dz in self.school_infos:
                    f.write(mc+"\t"+xd+"\t"+qy+"\t"+xz+"\t"+dh+"\t"+dz)    
            f.close()
            return len(self.school_infos)
            
        except Exception as e:
            print('[ERROR] Craw Field!Url:', downloading_url, 'Info:', e)
            # 利用traceback定位异常
            traceback.print_exc()

if __name__ == '__main__':
    obj_spider = CodeSpider()
    split_url = 'http://infomap.cdedu.gov.cn/Home/Index?all=1&pages='
    #一共123页
    sum=0
    for i in range(1,124):
        # print(split_url+str(i))
        sum=sum+obj_spider.craw(split_url+str(i))
        print("第"+str(i)+"页搞定")
    print("成功爬取"+str(sum)+"条数据")
