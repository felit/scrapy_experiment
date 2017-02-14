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
# driver = webdriver.Chrome()

begin = time.time()
browser.get('https://zhidao.baidu.com/')
browser.get('http://www.baidu.com/link?url=YHOkgG9s9BjtBpxAju3GB2xjJyXjUeEh-uQOf6_zLn6EYp7hFrFVnecTSfZDtErH')
print dir(browser)
# WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "ACCOUNT")))
end = time.time()
print(end - begin)
# window.scrollBy(0,10000) 6个
# browser.execute_script('for(var i =0;i<6;i++){ setInterval(function(){ window.scrollBy(0,10000)},2000)}')
time.sleep(5)
js = 'window.open("https://www.sogou.com");'
browser.execute_script(js)

print browser.window_handles
time.sleep(1)
browser.save_screenshot("vdisk.png")

end = time.time()
print(end - begin)

# browser.close()
browser.quit()

# 分阶段
