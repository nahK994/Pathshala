import pika
import json


params = pika.URLParameters('amqps://itqdjkpt:6GAMl22_0xjDtFVbmslqDEZ-mtqN7VqP@shrimp.rmq.cloudamqp.com/itqdjkpt')
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.exchange_declare(exchange='exchange', exchange_type='mail')

print("consumer online")
channel.start_consuming()