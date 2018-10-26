import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

LOGS_EXCHANGE = "logs"

channel.exchange_declare(exchange=LOGS_EXCHANGE, exchange_type='fanout')

# No queue declared! Receiver of logs must declare the queue. Exchange will drop messages.

message = ' '.join(sys.argv[1:]) or 'Hello world!'

channel.basic_publish(exchange=LOGS_EXCHANGE,
                      routing_key='',  # routing key ignored for fanout exchange
                      body=message,
                      properties=pika.BasicProperties(
                          delivery_mode=2  # make message persistent
                      ))

print("[x] Sent '{}'".format(message))

connection.close()
