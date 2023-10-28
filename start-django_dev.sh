#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset


# Start Django server
echo "Starting Django server ..." &
#sleep 5
python manage.py makemigrations
python manage.py migrate
# python manage.py collectstatic --no-input
python manage.py runserver 0.0.0.0:8000
