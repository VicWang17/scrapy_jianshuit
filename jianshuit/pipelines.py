# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class JianshuitPipeline(object):
    def __init__(self):
        conn = pymysql.connect(host = 'localhost',user = 'root',db = 'mydb',passwd='',port = 3306,charset = 'utf8')
        cursor = conn.cursor()
        self.post = cursor
    def process_item(self,item,spider):
        cursor = self.post
        cursor.execute("use mydb")
        sql = "insert into jianshu (USER,TIME,TITLE,VIEW,COMMENT,LIK,GAIN) values(%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql,(item['user'],item['time'],item['title'],item['view'],item['comment'],item['like'],item['gain']))
        cursor.connection.commit()
        return item
