# -*- coding:utf8 -*-
from scrapy.settings import Settings
from scrapy.crawler import CrawlerProcess
from twisted.internet import reactor

from spiders.proxy import ProxySpider

settings = Settings()
for i in range(1,5):

    runner = CrawlerProcess()
    crawler = runner.create_crawler(ProxySpider())
    crawler.crawl()
    # runner.start(True)
reactor.run()


