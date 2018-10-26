To listen to all message, `python receive_logs_topic.py "#"`.

To send a message with the `binding key` of `cheese` and the `message body` of `cheddar`, `python emit_log_topic.py "cheese" "cheddar"`.

To listen to messages that only deal with cheese, `python receive_logs_topic.py "cheese.*"`.

Send a message about gouda with `python emit_log_topic.py "cheese.gouda" "mmmm"`.

Note that `receive_logs_topic.py` picks up this message.

Send a message about vegan cheese with `python emit_log_topic.py "not_cheese.coconut_oil" "not sure"`.

Note that `receive_logs_topic.py` **does not** pick up this message. 