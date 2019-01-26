# CD_school_list_spider
爬取成都市中小学(幼儿园)学校信息,包含名称、学段、办学性质、电话、地址、所属区域

可爬取成都市所有中小学列表到文件或者数据库，文件路径和数据库需要自行配置
主文件：spiker_main.py或spider_main_sql.py 
有两种存储数据方式 1、爬取胡保存到mysql数据中，使用前需要先建立数据库和表（主文件：spider_main_sql.py） 2、保存到记事本文件，（主文件：spider_main.py）

需要在python3环境下运行
用到如下包： bs4 re urllib.request urllib.error requests random time traceback若没有可通过pip安装
