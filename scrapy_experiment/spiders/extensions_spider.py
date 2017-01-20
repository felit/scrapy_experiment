# -*- coding: utf-8 -*-
import scrapy

from scrapy_experiment.items import ScrapyexperimentItem
from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher


class ExtensionsSpider(scrapy.Spider):
    name = 'extentions'
    # custom_settings = {
    # 'EXTENSIONS': {
    # # 'scrapy_experiment.extensions.extentions_demo.ExtensionsDemo': 200
    # }
    # }
    start_urls = ['http://www.oschina.net/']
    custom_settings = {
        'DEFAULT_REQUEST_HEADERS': {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'Host': 'www.oschina.net',
            # 'Origin': 'http://www.dianping.com',
            # 'Referer': 'http://www.dianping.com/search/category/267/10',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.90 Safari/537.36',
        }
    }

    def __init__(self):
        # self.crawler.signals.connect(self.spider_opened, signals.spider_opened)
        dispatcher.connect(self.spider_opened, signals.spider_opened)

    def spider_opened(self, spider):
        print spider

    def parse(self, response):
        item = ScrapyexperimentItem()
        item['name'] = 'oschina.net.text'
        yield item
        print response.headers