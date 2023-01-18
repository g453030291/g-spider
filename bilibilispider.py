import json

import pymysql
import scrapy

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123456789',
                             database='spider',
                             cursorclass=pymysql.cursors.DictCursor)


class BilibiliSpider(scrapy.Spider):
    name = "bilibilispider"

    start_urls = ["https://api.bilibili.com/x/web-interface/popular?ps=20&pn=1"]

    def parse(self, response, **kwargs):
        with connection:
            with connection.cursor() as cursor:
                sql = "insert into bilibili (origin_json) values (%s)"
                cursor.execute(sql, (response.text,))
            connection.commit()
        data = json.loads(response.text)
        list = data['data']['list']
        i = 0
        for l in list:
            with connection:
                with connection.cursor() as cursor:
                    sql = "insert into detail (type,sort,context) values (%s, %s, %s)"
                    connection.ping(reconnect=True)
                    cursor.execute(sql, (2, i, l['title'],))
                connection.commit()
            ++i
