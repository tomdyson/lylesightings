#!/bin/bash
python manage.py migrate                  # Apply database migrations
python manage.py collectstatic --noinput  # Collect static files

# Start Gunicorn processes
exec gunicorn lylesightings.wsgi:application --bind 0.0.0.0:$PORT --workers 3
