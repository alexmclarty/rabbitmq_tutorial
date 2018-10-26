import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

LOGS_EXCHANGE = "logs"

channel.exchange_declare(exchange=LOGS_EXCHANGE, exchange_type='fanout')

result = channel.queue_declare(exclusive=True)  # once consumer dies, delete the queue.

# As no queue name was given, one is generated
queue_name = result.method.queue

channel.queue_bind(exchange=LOGS_EXCHANGE, queue=queue_name)

print('[*] Waiting for logs. To exist, CTRL+C...')


def callback(ch, method, properties, body):
    print("[x] %r" % body)


channel.basic_consume(callback, queue=queue_name, no_ack=True)

channel.start_consuming()
