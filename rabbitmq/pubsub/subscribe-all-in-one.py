# -*- coding:utf8 -*-
import pika
from time import sleep

con = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
cha = con.channel()
cha.exchange_declare(durable=False, exchange='yanfa2', type='fanout', )
result = cha.queue_declare(queue='sub', durable=True)
cha.queue_bind(exchange='yanfa2', queue=result.method.queue, routing_key='', )
cha.basic_qos(prefetch_count=1)
print ' [*] Waiting for messages. To exit press CTRL+C'


def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)
    ch.basic_ack(delivery_tag=method.delivery_tag)


def callback2(ch, method, properties, body):
    print " [x] Received %r" % (body,)
    # sleep(2)
    ch.basic_ack(delivery_tag=method.delivery_tag)

cha.basic_consume(callback, queue='sub', no_ack=False )


result = cha.queue_declare(queue='sub-one', durable=True)
cha.queue_bind(exchange='yanfa2', queue=result.method.queue, routing_key='', )
cha.basic_consume(callback2, queue='sub-one', no_ack=False )
cha.start_consuming()