# -*- coding: utf-8 -*-
import scrapy


class ProxySpider(scrapy.Spider):
    name = "proxy"
    allowed_domains = ["www.baidu.com"]
    start_urls = [
        'http://www.baidu.com/',
    ]

    def parse(self, response):
        print response.body
        pass
