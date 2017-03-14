# -*- coding:utf8 -*-
import pika
import sys
import time

credential = pika.PlainCredentials('weipan', 'weipan_admin')
# con = pika.BlockingConnection(pika.ConnectionParameters('localhost',credentials=credential, virtual_host='/weipan'))
con = pika.BlockingConnection(pika.ConnectionParameters('www.livedrof.com',credentials=credential, virtual_host='/weipan'))
channel = con.channel()
result = channel.queue_declare(durable=True, queue='crawler-test', exclusive=False)
channel.exchange_declare(exchange='baidu', type='fanout', durable=False)
channel.queue_bind(exchange='baidu', queue=result.method.queue, routing_key='')
for i in range(1,20):
    channel.basic_publish(exchange='baidu', routing_key='crawler-test', properties=pika.BasicProperties(delivery_mode=2, ),
                          body='durable')
con.close()
