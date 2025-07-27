#!/bin/bash

set -e

GUNICORN_TIMEOUT=${GUNICORN_TIMEOUT:-600}
GUNICORN_WORKERS=${GUNICORN_WORKERS:-2}
APP_PORT=${APP_PORT:-8100}

cd code

echo ">>> Running migrations..."
python manage.py migrate

echo ">>> Starting Django application..."
echo "APP PORT IS " $APP_PORT
#python manage.py runserver

gunicorn --bind 0.0.0.0:$APP_PORT app.wsgi --workers $GUNICORN_WORKERS --timeout $GUNICORN_TIMEOUT