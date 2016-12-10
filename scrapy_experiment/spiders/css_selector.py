# -*- coding: utf-8 -*-
import scrapy


class CssSelectorSpider(scrapy.Spider):
    name = "css_selector"
    allowed_domains = ["localhost"]
    start_urls = ['http://localhost:9000/css-selector.html']

    def parse(self, response):
        pass
