# RabbitMQ tutorial code

Tutorial code for https://www.rabbitmq.com/getstarted.html.

# Setup

## RabbitMQ

Run `docker-compose up` in the root directory to start RabbitMQ on your machine.

Management UI available at `localhost:15672` with `guest`/`guest`.

If you want to run commands on the container running RabbitMQ, connect with `docker exec -it <container-id> bash`.

## Python

Setup a virtualenv and install dependencies from `requirements.txt`.
