# -*- coding: utf-8 -*-
import scrapy

from scrapy_experiment.items import ScrapyexperimentItem
from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher
import logging

logger = logging.getLogger(__name__)


class ExtensionsSpider(scrapy.Spider):
    name = 'extensions'
    # custom_settings = {}
    start_urls = ['http://www.oschina.net/']
    custom_settings = {
        'FEED_URI':'file:///home/congsl/tmp/extensions.json',
        'FEED_FORMAT':'json',
         'EXTENSIONS': {
            # 'scrapy_experiment.extensions.extensions_traceback.ExtensionsTraceback': 200
        },
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

    def parse(self, response):
        item = ScrapyexperimentItem()
        item['name'] = 'oschina.net.text'
        yield item

    def __init__(self):
        # self.crawler.signals.connect(self.spider_opened, signals.spider_opened)
        dispatcher.connect(self.spider_opened, signals.spider_opened)
        dispatcher.connect(self.item_scraped, signal=signals.item_scraped)

    def spider_opened(self, spider):
        print spider

    def item_scraped(self, item, spider):
        logger.info('item_scraped methods:%s,%s', item, spider)


