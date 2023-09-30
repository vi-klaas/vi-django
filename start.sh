#!/bin/bash

# Start Dramatiq worker
python manage.py rundramatiq &

# Start Django server
#python manage.py tailwind start >> tailwind.log 2>&1 &
echo "Starting Django server after 5 seconds ..." &
#sleep 5
python manage.py runserver 0.0.0.0:8000