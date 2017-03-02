# -*- coding:utf8 -*-
import pika
import sys
import time

con = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
cha = con.channel()
result = cha.queue_declare(queue='sub', durable=True, exclusive=False)
cha.exchange_declare(durable=False, exchange='yanfa2', type='fanout', )
cha.queue_bind(exchange='yanfa2', queue=result.method.queue, routing_key='', )
begin_time = time.time()
for i in range(1, 10):
    cha.basic_publish(exchange='yanfa2',
                      routing_key='',
                      body='hello rabbitmq consumer%s' % (str(i)),
                      properties=pika.BasicProperties(delivery_mode=2, ))
end_time = time.time()
print 'take times:%sms' % (end_time - begin_time)
print '[x] Sent %r' % (' '.join(sys.argv[:]))
#关闭连接
con.close()