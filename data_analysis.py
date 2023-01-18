import datetime
import jieba
import datasource as db

if __name__ == "__main__":
    mysql = db.Mysql()
    # startDatetime = datetime.date.today().__str__() + " 00:00:00"
    # endDatetime = datetime.date.today().__add__(-1).__str__() + " 23:59:59"
    startDatetime = datetime.datetime(2023, 1, 8, 0, 0, 0).__str__()
    endDatetime = datetime.datetime(2023, 1, 8, 23, 59, 59).__str__()
    # 关键词解析
    result = mysql.select(
        sql="select * from detail where created_at between '" + startDatetime + "' and '" + endDatetime + "'")
    context = ''
    for r in result:
        context += r['context']
    # 分词
    wordcount = jieba.lcut(context)
    counts = {}
    for k in wordcount:
        if len(k) == 1:
            continue
        if counts.get(k) == None:
            counts.__setitem__(k, 1)
        else:
            counts[k] += 1
    result = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    print(result)
    # for r in result:
    #     print(r)
