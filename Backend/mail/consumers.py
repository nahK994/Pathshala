import pika
import json
from eventHandlers.registrationEvents import *


# params = pika.URLParameters('amqps://itqdjkpt:6GAMl22_0xjDtFVbmslqDEZ-mtqN7VqP@shrimp.rmq.cloudamqp.com/itqdjkpt')
# connection = pika.BlockingConnection(params)
params = pika.ConnectionParameters('0.0.0.0')
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.exchange_declare(exchange='exchange', exchange_type='topic')

queue1 = channel.queue_declare('', exclusive=True)
queue_name1 = queue1.method.queue
channel.queue_bind(exchange='exchange', queue=queue_name1, routing_key='invite_teacher_mail_by_admin')
channel.basic_consume(queue=queue_name1, on_message_callback=inviteTeacher, auto_ack=True)

print("consumer online")
channel.start_consuming()