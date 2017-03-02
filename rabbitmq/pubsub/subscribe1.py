# -*- coding:utf8 -*-
import pika

con = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
cha = con.channel()
result = cha.queue_declare(queue='sub1', durable=True)
cha.exchange_declare(durable=False, exchange='yanfa2', type='fanout', )
cha.queue_bind(exchange='yanfa2', queue=result.method.queue, routing_key='', )
cha.basic_qos(prefetch_count=1)
print ' [*] Waiting for messages. To exit press CTRL+C'


def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)
    ch.basic_ack(delivery_tag=method.delivery_tag)


cha.basic_consume(callback, queue='sub1', no_ack=False )
cha.start_consuming()