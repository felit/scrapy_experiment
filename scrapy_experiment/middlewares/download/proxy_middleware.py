# -*- coding:utf8 -*-


class ProxyMiddleware(object):
    def process_request(self, request, spider):
        print request.meta, request.url
        if 'proxy' not in request.meta:
            request.meta['proxy'] = "http://1.179.146.153:8080"
        # request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass
        pass

    def process_exception(self, request, exception, spider):
        # print request.meta
        print exception
        req = request.copy()
        if request.meta['proxy'] == 'http://1.179.146.153:8080':
            req.meta['proxy'] = 'http://103.18.180.94:8080'
        else:
            req.meta['proxy'] = 'http://115.254.104.206:8080'
        return req