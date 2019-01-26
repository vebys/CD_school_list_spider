# -*- coding: utf-8 -*-
import pymysql.cursors
class MysqlHandler(object):
    def __init__(self):
        self.db = pymysql.connect(host="127.0.0.1", user="vebys", passwd="root", db="gcjt", charset="utf8", cursorclass=pymysql.cursors.DictCursor)

    def insert(self,mc,xd,qy,xz,dh,dz):
        try:
            with self.db.cursor() as cursor:
                cursor.execute('REPLACE INTO school_list (`mc`, `xd`, `qy`, `xz`, `dh`, `dz`)  VALUES ( %s, %s, %s, %s, %s, %s)' , [mc,xd,qy,xz,dh,dz])                
            #insert_id = cursor.lastrowid
            self.db.commit()
        except Exception as e:
            raise Exception('MySQL ERROR:', e)
        # 返回存储后的id
        return mc+": success"

    #最后需要调用该方法来关闭连接
    def close(self):
        self.db.close()
