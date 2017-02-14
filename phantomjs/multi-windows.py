# -*- coding:utf8 -*-
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


"""
  杀掉phantomjs进程
  ps -ef | grep -i phan | grep -v grep | awk '{print $2}'| xargs kill -9
"""
browser = webdriver.PhantomJS()
begin = time.time()
browser.get('https://zhidao.baidu.com/')
end = time.time()
print(end - begin)
time.sleep(5)
js = 'window.open("https://www.sogou.com");'
browser.execute_script(js)
browser.switch_to.window(browser.window_handles[1])
time.sleep(5)
browser.save_screenshot("multi-windows.png")
browser.quit()
