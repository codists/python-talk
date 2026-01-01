import json
import re

import scrapy


class ManningSpider(scrapy.Spider):
    name = "manning"
    allowed_domains = ['www.manning.com']

    # 因为 headers 要给多个方法调用(如：start_requests(), parse())，所以声明未类变量
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

    def start_requests(self):
        """
        重写该方法以执行 POST 方法
        """

        yield scrapy.Request(
            url='https://www.manning.com/search/getCatalogData',
            method='POST',
            headers=self.headers,
            body=json.dumps(self.payload),
            callback=self.parse,
        )

    def parse_detail(self, response):
        """
        从详情页解析 ISBN 和 description（可选）
        """
        import time
        self.logger.info(f"parse_detail start {time.time()}")
        book = response.meta['book']

        # 获取 html 页面的 ISBN
        isbn_text = response.xpath(
            '//div[contains(@class,"product-meta")]'
            '//li[starts-with(normalize-space(),"ISBN")]/text()'
        ).get()
        m = re.search(r'ISBN(?:-13)?:?\s*([0-9\-]{10,17})',isbn_text)
        if m:
            book['isbn'] = m.group(1).replace('-', '')

        book['isbn'] = book.get('isbn') or None

        yield book

    def parse(self, response):
        """
        response: 将执行 start_requests() 里面的 scrapy.Request()得到的响应 作为这里的 response
        """
        data = response.json()
        books = data['products']
        for book in books:
            book['publisher'] = 'manning'
            yield scrapy.Request(
                url=book['link'],
                callback=self.parse_detail,
                meta={'book': book},
            )

        # 如果有下一页，且不是最后一页
        # and 的优先级高于 :=，所以前半部分用括号括起来
        if (pagination := data.get('pagination')) and pagination.get('hasNextPage'):
            payload = self.payload.copy()
            payload['page'] = pagination['page'] + 1

            yield scrapy.Request(
                url='https://www.manning.com/search/getCatalogData',
                method='POST',
                headers=self.headers,
                body=json.dumps(payload),
                callback=self.parse,
            )
