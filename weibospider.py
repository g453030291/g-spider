import pymysql
import scrapy
import json

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123456789',
                             database='spider',
                             cursorclass=pymysql.cursors.DictCursor)

class WeiboSpider(scrapy.Spider):
    name = "wspider"

    start_urls = [
        "https://weibo.com/ajax/statuses/hot_band"
    ]

    def parse(self, response, **kwargs):
        # print(response.text)
        with connection:
            with connection.cursor() as cursor:
                sql = "insert into weibo (origin_json) values (%s)"
                cursor.execute(sql, (response.text,))
            connection.commit()
        data = json.loads(response.text)
        # print(data["ok"])
        # print(data['http_code'])
        bandList = data['data']['band_list']
        for bl in bandList:
            # print('{0}---{1}'.format(bl['realpos'], bl['word']))
            realpos = bl['realpos']
            word = bl['word']
            with connection:
                with connection.cursor() as cursor:
                    sql = "insert into detail (type,sort,context) values (%s, %s, %s)"
                    connection.ping(reconnect=True)
                    cursor.execute(sql, (1, realpos, word,))
                connection.commit()