#!/usr/bin/env bash
set -e
python manage.py migrate --noinput
python manage.py collectstatic --noinput
gunicorn conquest.wsgi:application --bind 0.0.0.0:$PORT