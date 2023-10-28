#!/bin/bash

set -o errexit
set -o nounset

# Start Celery beat only after RabbitMQ server is up and running

rabbitmq_is_ready() {
# Use nc (Netcat) to check if we can access to the given host and port
nc -z rabbitmq 5672
}

until rabbitmq_is_ready; do
  echo 'Waiting for RabbitMQ server...'
  sleep 1
done

echo 'RabbitMQ server is ready. Starting Celery beat...'

rm -f './celerybeat.pid'
exec celery -A vidjango beat -l INFO
