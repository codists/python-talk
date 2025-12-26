# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


# class BooksbotPipeline:
#     def process_item(self, item, spider):
#         return item
from python_talk.models.book import Book
from python_talk.extensions import db

class BookPipeline:
    def process_item(self, item, spider):
        """
        将采集到的数据存入数据库
        """
        print(item)
        book = Book(**item)
        db.session.add(book)
        db.session.commit()

    def open_spider(self, spider):
        print('spider 打开')

    def close_spider(self, spider):
        print('spider 关闭')
