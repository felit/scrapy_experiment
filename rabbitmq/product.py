#-*- coding:utf8 -*-
import pika
import sys
#创建连接connection到localhost
con = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
#创建虚拟连接channel
cha = con.channel()
#创建队列anheng,durable参数为真时，队列将持久化；exclusive为真时，建立临时队列
result=cha.queue_declare(queue='anheng',durable=True,exclusive=False)
#创建名为yanfa,类型为fanout的exchange，其他类型还有direct和topic，如果指定durable为真，exchange将持久化
cha.exchange_declare(durable=False,
          exchange='yanfa',
          type='direct',)
#绑定exchange和queue,result.method.queue获取的是队列名称
cha.queue_bind(exchange='yanfa', 
       queue=result.method.queue,
       routing_key='',) 
#公平分发，使每个consumer在同一时间最多处理一个message，收到ack前，不会分配新的message
# cha.basic_qos(prefetch_count=)
#发送信息到队列‘anheng'
message = ' '.join(sys.argv[:])
#消息持久化指定delivery_mode=；
cha.basic_publish(exchange='',
         routing_key='anheng',
         body='hello world',
         properties=pika.BasicProperties(
          # delivery_mode = ,
        ))
print '[x] Sent %r' % (message,)
#关闭连接
con.close()