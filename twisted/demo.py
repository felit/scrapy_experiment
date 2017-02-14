# -*- coding: utf-8 -*-
from twisted.web.client import getPage
from twisted.internet import reactor

"""
说明:
1. Python中, 注释一般是用 ''' 这种方式 ''' 的.
2. 没有{}来表示运行块, 用indent的深度来识别; 不适用分号来表示语句结束.
3. 指定encode的标记十分特别.
4. callback方式的.
5. Deferred对象来自于twisted.internet.defer.Deferred.
6.Python是case sensitive...

"""
def printContents(contents):
    print "获得内容:"
    print contents.upper()

    reactor.stop()


def errorHandler(error):
    print error

    reactor.stop()

# 请求
deferred = getPage("http://www.baidu.com")
#添加回调
deferred.addCallback(printContents)
deferred.addErrback(errorHandler)
#反应堆~
reactor.run()