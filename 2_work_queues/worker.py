import time

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()
channel.queue_declare(queue='task-queue', durable=True)


def callback(ch, method, properties, body):
    print("[x] Received %r " % body)
    sleep_time = body.count(b'.')
    print("\tSleeping for {}s... ".format(sleep_time))
    time.sleep(sleep_time)
    # ack the message
    # must be sent on the same channel the delivery it is for was received on.
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback, queue='hello')  # no_ack=True
print('[*] Waiting for messages. To exit press CTRL+C...')
channel.start_consuming()
