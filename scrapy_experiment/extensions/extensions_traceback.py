# -*- coding:utf-8 -*-
from scrapy import signals
import traceback
from scrapy.exceptions import NotConfigured
import logging

logger = logging.getLogger(__name__)


class ExtensionsTraceback():
    def __init__(self, crawler):
        crawler.signals.connect(self.engine_started, signal=signals.engine_started)
        crawler.signals.connect(self.engine_stopped, signal=signals.engine_stopped)
        crawler.signals.connect(self.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(self.spider_idle, signal=signals.spider_idle)
        crawler.signals.connect(self.spider_closed, signal=signals.spider_closed)
        crawler.signals.connect(self.spider_error, signal=signals.spider_error)
        crawler.signals.connect(self.request_scheduled, signal=signals.request_scheduled)
        crawler.signals.connect(self.request_dropped, signal=signals.request_dropped)
        crawler.signals.connect(self.response_received, signal=signals.response_received)
        crawler.signals.connect(self.response_downloaded, signal=signals.response_downloaded)
        crawler.signals.connect(self.item_scraped, signal=signals.item_scraped)
        crawler.signals.connect(self.item_dropped, signal=signals.item_dropped)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)
        # 拋出此异常　扩展会被禁用
        # raise NotConfigured()


    def engine_started(self):
        traceback.print_stack()
        logger.info("engine_started:%s", self)

    def engine_stopped(self):
        logger.info("engine_stopped:%s", self)

    def spider_opened(self, spider):
        logger.info("spider:%s", spider)

    def spider_idle(self):
        traceback.print_stack()

    def spider_closed(self, spider, reason):
        pass

    def spider_error(self, failure, response, spider):
        pass

    def request_scheduled(self):
        pass

    def request_dropped(self):
        pass

    def response_received(self, response, request, spider):
        pass

    def response_downloaded(self, response, request, spider):
        pass

    def item_scraped(self, item, spider):
        logger.info('crawl items:%s', item)

    def item_dropped(self, item, spider, exception):
        pass