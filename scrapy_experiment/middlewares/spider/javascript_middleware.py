# -*- coding:utf8 -*-
from selenium import webdriver
from scrapy.http import HtmlResponse
import time


class JavaScriptMiddleware(object):
    def process_spider_output(self, response,result, spider):
        print"PhantomJS is starting..."
        driver = webdriver.PhantomJS()  # 指定使用的浏览器
        # driver = webdriver.Firefox()
        driver.get(response.url)
        time.sleep(1)
        js = "var q=document.documentElement.scrollTop=10000"
        driver.execute_script('document.title')  # 可执行js，模仿用户操作。此处为将页面拉至最底端。
        time.sleep(3)
        body = driver.page_source
        print("访问" + response.url)
        return HtmlResponse(driver.current_url, body=body, encoding='utf-8', request=response)