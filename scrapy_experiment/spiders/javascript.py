# -*- coding: utf-8 -*-
import scrapy


class JavascriptsSpider(scrapy.Spider):
    name = "javascript"
    allowed_domains = ["bj.lianjia.com"]
    start_urls = ['http://bj.lianjia.com/']

    def parse(self, response):
        print response.url
        pass
