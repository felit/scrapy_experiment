# -*- coding:utf8 -*-
from selenium import webdriver
from selenium.webdriver.common.proxy import ProxyType
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

browser = webdriver.PhantomJS()


def print_info(browser):
    print browser.page_source.encode('UTF-8', 'ignore')
    """
         [{u'domain': u'.meituan.com', u'name': u'oc', u'expires': u'\u5468\u56db, 07 2\u6708 2047 02:22:03 GMT',
         u'value': u'qC738wrXrgTWAbqKoCsyYmUo4gTZZXiURXb9dVPtWgt68HXYP5j8sIRjjUeklT6xQgUvrYnMRrWgiz3ccVDy1K7Td-HBUloKPOSHmJgjerS1CDQjbVr_OnJJ97Jap_H256dgDpw5GfibxZ0SZJf0lFlWBs3ekzxQud-ICu54ews',
         u'expiry': 2433118923, u'path': u'/', u'httponly': False, u'secure': False},
         {u'domain': u'.meituan.com', u'name': u'uuid', u'expires': u'\u5468\u56db, 07 2\u6708 2047 02:22:03 GMT',
         u'value': u'94f99c0baca6499e5eeb.1487038921.0.0.0', u'expiry': 2433118923, u'path': u'/', u'httponly': False, u'secure': False},
         {u'domain': u'.meituan.com', u'name': u'__mta', u'expires': u'\u5468\u4e00, 04 2\u6708 2019 02:22:21 GMT',
         u'value': u'50637206.1487038941895.1487038941895.1487038941895.1', u'expiry': 1549246941, u'path': u'/',
         u'httponly': False, u'secure': False}, {u'domain': u'.meituan.com', u'name': u'__utmv',
         u'expires': u'\u5468\u56db, 14 2\u6708 2019 02:22:21 GMT', u'value': u'211559370.|1=city=bj=1',
         u'expiry': 1550110941, u'path': u'/', u'httponly': False, u'secure': False},
         {u'domain': u'.meituan.com', u'name': u'__utmz', u'expires': u'\u5468\u4e8c, 15 8\u6708 2017 14:22:21 GMT',
         u'value': u'211559370.1487038942.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)', u'expiry': 1502806941,
         u'path': u'/', u'httponly': False, u'secure': False}, {u'domain': u'.meituan.com', u'name': u'__utmc',
         u'value': u'211559370', u'path': u'/', u'httponly': False, u'secure': False},
         {u'domain': u'.meituan.com', u'name': u'__utmb', u'expires': u'\u5468\u4e8c, 14 2\u6708 2017 02:52:21 GMT',
         u'value': u'211559370.1.10.1487038942', u'expiry': 1487040741, u'path': u'/', u'httponly': False, u'secure': False},
         {u'domain': u'.meituan.com', u'name': u'__utma', u'expires': u'\u5468\u56db, 14 2\u6708 2019 02:22:21 GMT',
         u'value': u'211559370.334250871.1487038942.1487038942.1487038942.1', u'expiry': 1550110941, u'path': u'/', u'httponly':
         False, u'secure': False}, {u'domain': u'.meituan.com', u'name': u'_lxsdk_s', u'expires': u'\u5468\u4e09,
         15 2\u6708 2017 08:22:21 GMT', u'value': u'f5ae88521506f3de757358772ecb%7C%7C0', u'expiry': 1487146941, u'path': u'/',
         u'httponly': False, u'secure': False}, {u'domain': u'.meituan.com', u'name': u'abt',
         u'expires': u'\u5468\u56db, 07 2\u6708 2047 02:22:01 GMT', u'value': u'1487038921.0%7CADE',
         u'expiry': 2433118921, u'path': u'/', u'httponly': False, u'secure': False}, {u'domain': u'.meituan.com',
         u'name': u'ci', u'expires': u'\u5468\u56db, 07 2\u6708 2047 02:22:01 GMT', u'value': u'1',
         u'expiry': 2433118921, u'path': u'/', u'httponly': False, u'secure': False}]
    """
    print browser.get_cookies()
    print browser.title
    """
       {u'rotatable': False, u'takesScreenshot': True, u'acceptSslCerts': False,
       u'browserConnectionEnabled': False, u'javascriptEnabled': True, u'driverVersion': u'1.2.0', u'databaseEnabled': False,
       u'locationContextEnabled': False, u'platform': u'linux-unknown-64bit', u'browserName': u'phantomjs', u'version': u'2.1.1',
       u'driverName': u'ghostdriver', u'nativeEvents': True, u'applicationCacheEnabled': False,
       u'webStorageEnabled': False, u'proxy': {u'proxyType': u'direct'}, u'handlesAlerts': False, u'cssSelectorsEnabled': True}
    """
    print browser.capabilities
    print browser.current_url
    # <selenium.webdriver.common.html5.application_cache.ApplicationCache object at 0x7fd6ab212ad0>
    print browser.application_cache


browser.get('http://bj.meituan.com/category/meishi?mtt=1.index%2Ffloornew.nc.1.iz46epfq')
WebDriverWait(browser, 10).until(expected_conditions.presence_of_element_located((By.TAG_NAME, 'body')))
browser.save_screenshot('browser-info.png')
print_info(browser)
browser.quit()