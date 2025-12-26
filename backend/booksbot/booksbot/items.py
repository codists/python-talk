# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# class BooksbotItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass

class BookItem(scrapy.Item):
    # 书名
    title = scrapy.Field()
    # 作者
    author = scrapy.Field()
    # 出版日期
    price = scrapy.Field()
    # 描述
    description = scrapy.Field()
    # 书籍详情页
    url = scrapy.Field()
