from scrapy.cmdline import execute


if __name__ == '__main__':
    print('start crawl manning books')
    execute(['scrapy', 'crawl', 'manning'])