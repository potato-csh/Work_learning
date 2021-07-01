# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class QiutuproPipeline(object):
    fp = None
    # 重写父类一个方法：该方法只有开始爬虫的时候被调用一次
    def open_spider(self, spider):
        print('开始爬虫......')
        self.fp = open('./qiubai.txt', 'w', encoding='utf-8')

    # 专门来处理item类型对象
    # 该方法可以接收爬虫文件提交过来的item对象
    # 该方法每接收一个item就会被调用一次
    def process_item(self, item, spider):
        author = item['author']
        content = item['content']

        self.fp.write(author + ':' + content + '/n')

        return item  # 就会传递给下一个即将被执行的管道类

    def close_spider(self, spider):
        print('结束爬虫......')
        self.fp.close()

# 管道文件中一个管道类对应将一组数据存储到一个平台或者载体中
class mysqlPipeline(object):
    conn = None
    cursor = None

    def open_spider(self, spider):
        self.conn = pymysql.Connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='password',
            db='qiutu',
            charset='utf8')

    def process_item(self, item, spider):
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute('insert into qiutu value("%s","%s")' % (item["author"], item["content"]))
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
