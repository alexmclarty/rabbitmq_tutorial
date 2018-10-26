Run `python receive_logs_direct.py error`, which will only listen for `error` messages.

Run `python emit_log.py error "some error message"`.

Note that `receive_logs_direct.py` picks up the message.

Run `python emit_log.py info "whatever"`.

Note that `receive_logs_direct.py` **does not** pick up the message.