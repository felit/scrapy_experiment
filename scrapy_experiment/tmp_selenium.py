#-*- coding:utf8 -*-
from selenium import webdriver
driver = webdriver.PhantomJS()
driver.get('http://www.baidu.com/')
res = driver.execute_script('document.title')
body = driver.page_source
print res
# print body
# selenium.common.exceptions.WebDriverException: Message: Error -
#  Unable to load Atom 'execute_script' from file ':/ghostdriver/./third_party/webdriver-atoms/execute_script.js'