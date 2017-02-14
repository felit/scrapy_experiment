# -*- coding:utf8 -*-
from selenium import webdriver
from selenium.webdriver.common.proxy import ProxyType
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

browser = webdriver.PhantomJS()
# driver = webdriver.Chrome()
"""
代理设置
"""
proxy = webdriver.Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = '1.9.171.51:800'
# 将代理设置添加到webdriver.DesiredCapabilities.PHANTOMJS中
proxy.add_to_capabilities(webdriver.DesiredCapabilities.PHANTOMJS)
browser.start_session(webdriver.DesiredCapabilities.PHANTOMJS)
"""
代理设置结束
"""
begin = time.time()
browser.get('http://bj.meituan.com/category/meishi?mtt=1.index%2Ffloornew.nc.1.iz46epfq')
# WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "ACCOUNT")))
end = time.time()
print(end - begin)
# window.scrollBy(0,10000) 6个
browser.execute_script('for(var i =0;i<6;i++){ setInterval(function(){ window.scrollBy(0,10000)},2000)}')
time.sleep(45)
print browser.page_source.encode('UTF-8', 'ignore')

browser.save_screenshot("meituan.png")
end = time.time()
print(end - begin)
print(browser.title)
# browser.close()
browser.quit()
