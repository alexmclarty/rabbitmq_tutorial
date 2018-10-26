Start two `workers`. Send messages with `new_task`.

Note that messages are sent round-robin to each `worker`.

Try sending a message that causes a long running task. Kill that task and note how RabbitMQ redelivers the unacked task to another worker. 