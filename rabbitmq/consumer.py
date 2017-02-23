# -*- coding:utf8 -*-
import pika
#创建连接connection到localhost
con = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
#创建虚拟连接channel
cha = con.channel()
#创建队列anheng
result = cha.queue_declare(queue='anheng', durable=True)
#创建名为yanfa,类型为fanout的交换机，其他类型还有direct和topic
cha.exchange_declare(durable=False, exchange='yanfa', type='direct', )
#绑定exchange和queue,result.method.queue获取的是队列名称
cha.queue_bind(exchange='yanfa', queue=result.method.queue, routing_key='', )
#公平分发，使每个consumer在同一时间最多处理一个message，收到ack前，不会分配新的message
cha.basic_qos(prefetch_count=1)
print ' [*] Waiting for messages. To exit press CTRL+C'
#定义回调函数
def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)
    ch.basic_ack(delivery_tag=method.delivery_tag)


cha.basic_consume(callback,
                  queue='anheng',
                  no_ack=False, )
cha.start_consuming()