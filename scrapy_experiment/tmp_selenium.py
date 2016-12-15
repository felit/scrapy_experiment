#-*- coding:utf8 -*-
from selenium import webdriver
driver = webdriver.PhantomJS()
driver.get('http://www.baidu.com/')
res = driver.execute_script('document.body')
body = driver.page_source
print res
print body
# selenium.common.exceptions.WebDriverException: Message: Error -
# Unable to load Atom 'execute_script' from file ':/ghostdriver/./third_party/webdriver-atoms/execute_script.js'
#
# from selenium import webdriver
#
# browser = webdriver.PhantomJS()
#
# browser.get("http://www.baidu.com")
# browser.find_element_by_id("kw").clear()
# browser.find_element_by_id("kw").send_keys("selenium")
# browser.find_element_by_id("su").click()
# browser.quit()