# -*- coding:utf8 -*-
import jieba
import redis

print dir(jieba)
seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
# seg_list = jieba.cut("明代4 其他 中国历代山水画.zip",cut_all=False)
seg_list = jieba.cut_for_search("明代4 其他 中国历代山水画.zip")
seg_list = jieba.cut_for_search("魏晋南北朝广东佛教的传播与分布_徐强.caj")
print "Full Mode:", "/".join(seg_list)


def arr(seg):
    a = []
    # while


from pymongo import MongoClient

client = MongoClient()
db = client.weipan
coll = db.files_size1
cursor = coll.find()
record = cursor.next()

pool = redis.ConnectionPool(host='localhost', port=6379)
r = redis.Redis(connection_pool=pool)
while record is not None:
    title = record['title']
    seg = jieba.cut(title)

    for word in seg:
        r.zadd('tokens', word, 1.0)
    record = cursor.next()
print r.smembers('tokens')

client.close()