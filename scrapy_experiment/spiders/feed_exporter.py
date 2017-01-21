# -*- coding: utf-8 -*-
import scrapy


class FeedExporterSpider(scrapy.Spider):
    name = "feed_exporter"
    allowed_domains = ["www.oschina.net"]
    start_urls = ['http://www.oschina.net/']
    custom_settings = {
        'FEED_URI': 'file:///home/congsl/tmp/extensions.json',
        'FEED_FORMAT': 'json'
    }

    def parse(self, response):

        pass
