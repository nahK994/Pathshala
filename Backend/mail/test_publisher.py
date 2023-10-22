import pika
import json

# params = pika.URLParameters('amqps://itqdjkpt:6GAMl22_0xjDtFVbmslqDEZ-mtqN7VqP@shrimp.rmq.cloudamqp.com/itqdjkpt')
# connection = pika.BlockingConnection(params)
params = pika.ConnectionParameters('0.0.0.0')
connection = pika.BlockingConnection(params)
channel = connection.channel()
data = json.dumps({
    "key": "data"
})
channel.exchange_declare(exchange='exchange', exchange_type='topic')
channel.basic_publish(exchange='exchange', routing_key='invite_teacher_mail_by_admin', body=data)

print("event sent.....")