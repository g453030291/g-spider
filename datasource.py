import pymysql


class Mysql(object):
    def __init__(self):
        connection = pymysql.connect(host='localhost', user='root', password='123456789', database='spider',
                                     cursorclass=pymysql.cursors.DictCursor)
        self.cursor = connection.cursor()

    def select(self, sql):
        self.cursor.connection.ping(reconnect=True)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def insert(self, sql, *args):
        self.cursor.connection.ping(reconnect=True)
        self.cursor.execute(sql, *args)
        return self.cursor.connection.commit()
