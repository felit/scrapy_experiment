# -*- coding:utf8 -*-
import pika
import sys
import time

# 创建连接connection到localhost
con = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
#创建虚拟连接channel
cha = con.channel()
#创建队列anheng,durable参数为真时，队列将持久化；exclusive为真时，建立临时队列
result = cha.queue_declare(queue='anheng', durable=True, exclusive=False)
#创建名为yanfa,类型为fanout的exchange，其他类型还有direct和topic，如果指定durable为真，exchange将持久化
cha.exchange_declare(durable=False, exchange='yanfa', type='direct', )
#绑定exchange和queue,result.method.queue获取的是队列名称
cha.queue_bind(exchange='yanfa', queue=result.method.queue, routing_key='', )
#公平分发，使每个consumer在同一时间最多处理一个message，收到ack前，不会分配新的message
# cha.basic_qos(prefetch_count=)
#发送信息到队列‘anheng'
# message = ' '.join(sys.argv[:])
#除了要声明queue是持久化的外，还需声明message是持久化的
#basic_publish的properties参数指定message的属性
#此处pika.BasicProperties中的delivery_mode=2指明message为持久的
#这样一来RabbitMQ崩溃重启后queue仍然存在其中的message也仍然存在
#需注意的是将message标记为持久的并不能完全保证message不丢失，因为
#从RabbitMQ接收到message到将其存储到disk仍需一段时间，若此时RabbitMQ崩溃则message会丢失
#况且RabbitMQ不会对每条message做fsync动作
#可通过publisher confirms实现更强壮的持久性保证
begin_time = time.time()
for i in range(1, 100):
    cha.basic_publish(exchange='',
                      routing_key='anheng',
                      body='hello rabbitmq consumer%s' % (str(i)),
                      properties=pika.BasicProperties(delivery_mode=2, ))
end_time = time.time()
print 'take times:%sms' % (end_time - begin_time)
print '[x] Sent %r' % (' '.join(sys.argv[:]))
#关闭连接
con.close()