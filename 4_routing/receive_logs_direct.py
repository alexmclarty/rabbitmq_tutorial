import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

LOGS_EXCHANGE = "direct_logs"

channel.exchange_declare(exchange=LOGS_EXCHANGE, exchange_type='direct')

result = channel.queue_declare(exclusive=True)  # once consumer dies, delete the queue.

# As no queue name was given, one is generated
queue_name = result.method.queue

severities = sys.argv[1:]
if not severities:
    sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
    sys.exit(1)

for severity in severities:
    channel.queue_bind(exchange=LOGS_EXCHANGE, queue=queue_name, routing_key=severity)

print('[*] Waiting for logs. To exist, CTRL+C...')


def callback(ch, method, properties, body):
    print("[x] %r:%r" % (method.routing_key, body))


channel.basic_consume(callback, queue=queue_name, no_ack=True)

channel.start_consuming()
