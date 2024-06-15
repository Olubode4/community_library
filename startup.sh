#!/bin/bash
# Apply database migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --no-input

# Start Gunicorn server
gunicorn locallibrary.wsgi:application --bind 0.0.0.0:8000
