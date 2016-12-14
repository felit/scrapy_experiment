# -*- coding: utf-8 -*-
import scrapy


class CssSelectorSpider(scrapy.Spider):
    name = "css_selector"
    allowed_domains = ["localhost"]
    start_urls = [
        'http://localhost:9000/css-selector.html',
    ]

    def parse(self, response):
        print response.css('.parent').extract()
        print response.css('div:not(.child)')
        print response.css('[class^="desc"]').extract()
        print response.css('[class$="div"]').extract()
        print response.css('[class~="attr"]').extract()
        print response.css('[class|="desc"]').extract()
        print response.css('[class*="esc"]').extract()
        print response.css('[attr]').extract()
        print response.css('.parent:nth-child(1)').extract()
        pass
