import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123456789',
                             database='spider',
                             cursorclass=pymysql.cursors.DictCursor)

# with connection:
#     with connection.cursor() as cursor:
#         sql = "insert into weibo (word) values (%s)"
#         cursor.execute(sql, 'test')
#         connection.commit()

if __name__ == "__main__":
    with connection:
        with connection.cursor() as cursor:
            sql = "insert into weibo (word) values (%s)"
            cursor.execute(sql, ('test',))
        connection.commit()