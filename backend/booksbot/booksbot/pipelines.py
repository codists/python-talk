# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from datetime import datetime

from booksbot.utils import extract_authors
from sqlalchemy import select

from python_talk.app import create_app
from python_talk.extensions import db
from python_talk.models.book import Book, Author


# class BooksbotPipeline:
#     def process_item(self, item, spider):
#         return item


class BookPipeline:
    def process_item(self, item, spider):
        """
        将采集到的数据存入数据库
        """
        # print(item)
        with self.app.app_context():

            # 判断作者是否存在,存在就存储(暂不考虑是否为同一作者)，不存在就新增
            author_name = item.get('authorshipDisplay')
            author_lst = extract_authors(author_name)

            authors = []
            for name in author_lst:
                stmt = select(Author).where(Author.name == name)
                author = db.session.execute(stmt).scalar_one_or_none()

                if not author:
                    author = Author(name=name)
                    db.session.add(author)
                    db.session.flush()

                authors.append(author)

            isbn = item.get("isbn")

            stmt = select(Book).where(Book.isbn == isbn)
            existing_book = db.session.execute(stmt).scalar_one_or_none()
            if not existing_book:
                book_data = {
                    'title': item['title'],
                    'isbn': item.get('isbn'),
                    'price': item['price'],
                    'url': item['link'],
                    'publisher': item['publisher'],
                    'publication_date': datetime.strptime(item['date'], "%Y-%m-%dT%H:%M:%S%z").date(),
                }
                book = Book(**book_data)
                book.authors = authors

                db.session.add(book)
            else:
                existing_book.title = item['title']
                existing_book.price = item['price']
                existing_book.url = item['link']
                existing_book.publisher = item['publisher']
                existing_book.publication_date = datetime.strptime(item['date'], "%Y-%m-%dT%H:%M:%S%z").date()
                # 先清空现有作者关系，然后重新建立
                existing_book.authors.clear()
                existing_book.authors.extend(authors)
                existing_book.image_url = item['imageUrl']

            db.session.commit()

    def open_spider(self, spider):
        # print('spider 打开')
        self.app = create_app()

    def close_spider(self, spider):
        # print('spider 关闭')
        with self.app.app_context():
            db.session.remove()

# if __name__ == '__main__':
#     app = create_app()
#     with app.app_context():
#         item = {
#             "title": "Generative AI in Action",
#             "author": "Alessandro Negro with Vlastimil Kus, Giuseppe Futia and Fabio Montagna<br><i>Forewords by Maxime Labonne, Khalifeh AlJadda<\u002fi>",
#             "price": 47.99,
#             "url": "https://www.manning.com/books/generative-ai-in-action",
#             "description": None,
#             "publisher": "manning",
#             'isbn': '9781617291326',
#             'date': "2020-11-29T00:00:00-0500",
#         }
#         pipeline = BookPipeline()
#         pipeline.process_item(item, spider=None)
