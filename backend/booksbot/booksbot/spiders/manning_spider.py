import json

import scrapy
from twisted.web.xmlrpc import payloadTemplate


class ManningSpider(scrapy.Spider):
    name = "manning"
    allowed_domains = ['www.manning.com']

    def start_requests(self):
        """
        重写该方法以执行 POST 方法
        """
        headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/120.0 Safari/537.36',
            'Accept': 'application/json, text/plain, */*',
            'Origin': 'https://www.manning.com',
            'Referer': 'https://www.manning.com/',
        }
        payload = {
            "accessType": [],
            # keywords: 书名里包含的关键字
            "keywords": [],
            "level": [],
            "meapFilter": "published",
            "productType": [
                "book"
            ],
            "programmingLanguages": [
                "python"
            ],
            "selectedCategoryIds": [
                1
            ],
            "sort": "newest",
            "includePrices": True
        }

        yield scrapy.Request(
            url='https://www.manning.com/search/getCatalogData',
            method='POST',
            headers=headers,
            body=json.dumps(payload),
            # cookies=cookies,
            callback=self.parse,
            # meta={'page': self.start_page, 'payload': payload},
        )

    def parse(self, response):
        data = response.json()
        books = data['products']
        for book in books:
            item_data = {
                'title': book['title'],
                'author': book['authorshipDisplay'],
                'price': book['price'],
                'url': book['link'],
                'description': None,
                'publisher': 'manning',
            }
            yield item_data
