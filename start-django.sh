#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset


# Start Django server
echo "Starting Django server ..." &
#sleep 5
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --no-input


# Check if DEBUG is set to true
if [ "$DJANGO_DEBUG" = "True" ]; then
    echo "Starting Django development server"
    python manage.py runserver 0.0.0.0:8000
else
    echo "Starting Gunicorn server"
    gunicorn vidjango.wsgi:application --bind 0.0.0.0:8000
fi
