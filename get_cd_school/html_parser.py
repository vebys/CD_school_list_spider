# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re


class HtmlParser(object):
    # 第一个参数：需要解析的html代码
    # 第二个参数：用于拼装下级页面的url
    def province_parser(self, html_content):
        if html_content is None:
            raise Exception('Html is None')
        # # 将html代码从gb2312转码到utf-8
        # html_content = html_content.encode('utf-8')
        soup = BeautifulSoup(html_content, 'html.parser')
        # 找出页面中所有有效数据
        uls = soup.find_all('ul', attrs={"class":"index_ul01"})
        # print("ul success")
        # 最终返回的数组  
        school_infos=[]
        # 暂存每个学校，因为一个ul里面有多个li
        school_info=[]
        # 暂存学校其他信息，因为一个ul里面有多个li
        school_info_li=[]
        for ul in uls:
            lis = ul.find_all("li")
            for li in lis:
                #把标题加入数组
                school_info.append(li.h1.get_text())
                # print(li.h1.get_text())
                # print(lis);
                # exit()
                ps = li.find_all('p')
                i=0
                ps_len= len(ps);
                # if ps_len==4:
                #     ps.insert(3,"<p>【无】无</p>")
                # print(ps)
                for p in ps:
                    if i<5:
                        p_list =p.get_text().replace("【","").split("】")
                        school_info.append(p_list[1])
                    i=i+1
                    # print(i)
                    # print(p_list[1])
                    # exit()
                # print(school_info)
                if ps_len==4:
                    school_info.insert(4,"无")
                if ps_len==5:
                    if(school_info[4][0:1].isdigit()):
                        pass
                    else:

                        # print(school_info[4][0:1].isdigit())
                        # print(school_info[4][0:1])
                        # print(school_info[4])
                        school_info[4]="无"
                # print(school_infos)
                school_info_li.append(school_info)
                school_info=[]
                # print(school_info_li[0])
                # exit()
            # print(school_info_li) 
            
            for row_li in school_info_li:

                school_infos.append(row_li)
            school_info_li=[]
            # print(school_infos)
            # exit()
            # print(school_infos)
        # print(school_info_li)
        # 返回当前页面所有学校信息的数组
        return school_infos
        

    # def city_parser(self, html_content, url):
    #     if html_content is None:
    #         raise Exception('Html is None')
    #     html_content = html_content.encode('utf-8')
    #     soup = BeautifulSoup(html_content, 'html.parser')
    #     # 找出“杭州市”、“温州市”等<tr>标签
    #     url_trs = soup.find_all('tr', 'citytr')
    #     # 生成包含市名称、下级url、市级12位编码的元组的列表
    #     urls = [(tr.contents[1].get_text() if tr.contents[1].a is None else tr.contents[1].a.get_text(),
    #               None if tr.contents[0].a is None else url + tr.contents[0].a['href'],
    #              tr.contents[0].get_text() if tr.contents[0].a is None else tr.contents[0].a.get_text())
    #             for tr in url_trs]
    #     print("解析 市 成功")
    #     return urls

    # def county_parser(self, html_content, url):
    #     if html_content is None:
    #         raise Exception('Html is None')
    #     #html_content = html_content.decode('gb2312', 'ignore').encode('utf-8')
    #     html_content = html_content.encode('utf-8')
    #     soup = BeautifulSoup(html_content, 'html.parser' )
    #     # 找出“上城区”、“下城区”等<tr>标签
    #     url_trs = soup.find_all('tr', 'countytr')
    #     # 生成包含区名称、下级url、区级12位编码的元组的列表
    #     urls = [(tr.contents[1].get_text() if tr.contents[1].a is None else tr.contents[1].a.get_text(),
    #               None if tr.contents[0].a is None else url + tr.contents[0].a['href'],
    #              tr.contents[0].get_text() if tr.contents[0].a is None else tr.contents[0].a.get_text())
    #             for tr in url_trs]
    #     print("解析 县 成功")
    #     return urls

    # def town_parser(self, html_content, url):
    #     if html_content is None:
    #         raise Exception('Html is None')
    #     html_content = html_content.encode('utf-8')
    #     soup = BeautifulSoup(html_content, 'html.parser' )
    #     # 找出“西湖街道”、“留下街道”等<tr>标签
    #     url_trs = soup.find_all('tr', 'towntr')
    #     # 生成包含乡镇街道名称、下级url、乡镇街道级12位编码的元组的列表
    #     urls = [(tr.contents[1].get_text() if tr.contents[1].a is None else tr.contents[1].a.get_text(),
    #               None if tr.contents[0].a is None else url + tr.contents[0].a['href'],
    #              tr.contents[0].get_text() if tr.contents[0].a is None else tr.contents[0].a.get_text())
    #             for tr in url_trs]
    #     print("解析 镇 成功")
    #     return urls
