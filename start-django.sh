#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset


# Start Django server
echo "Starting Django Production Server ..." &
#sleep 5
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --no-input
gunicorn vidjango.wsgi:application --bind 0.0.0.0:8000
