# -*- coding:utf8 -*-
import pika
import sys
import time

credential = pika.PlainCredentials('weipan', 'weipan_admin')
# con = pika.BlockingConnection(pika.ConnectionParameters('localhost',credentials=credential, virtual_host='/weipan'))
con = pika.BlockingConnection(pika.ConnectionParameters('localhost',credentials=credential, virtual_host='/weipan'))
channel = con.channel()
result = channel.queue_declare(durable=True, queue='crawler-test', exclusive=False)
channel.exchange_declare(exchange='baidu', type='fanout', durable=False)
channel.queue_bind(exchange='baidu', queue=result.method.queue, routing_key='')
channel.basic_publish(exchange='baidu', routing_key='crawler-test', properties=pika.BasicProperties(delivery_mode=2, ),
                      body='durable')
channel.basic_qos(prefetch_count=1)
print ' [*] Waiting for messages. To exit press CTRL+C'
#定义回调函数
def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(callback, queue='crawler-test', no_ack=False, )

channel.start_consuming()
con.close()
