# -*- coding: utf-8 -*-
import scrapy


class OschinaSpider(scrapy.Spider):
    name = "oschina"
    allowed_domains = ["www.oschina.net"]
    start_urls = ['http://www.oschina.net/']
    custom_settings = {
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
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.90 Safari/537.36',
        }
    }

    def parse(self, response):
        pass
