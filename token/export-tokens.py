# -*- coding:utf8 -*-
import jieba
import redis

pool = redis.ConnectionPool(host='localhost', port=6379)
r = redis.Redis(connection_pool=pool)
file = open('tokens.txt', 'w+')
for token in r.smembers('tokens'):
    file.write('{token}\n'.format(token=token))