#!/bin/bash

# Exit on error
set -e

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Creating directories..."
mkdir -p staticfiles
mkdir -p media
mkdir -p api

echo "Setting up environment..."
export DJANGO_SETTINGS_MODULE=ecommerce.settings_prod
export PYTHONPATH=/var/task:$PYTHONPATH

echo "Collecting static files..."
python manage.py collectstatic --noinput --clear

echo "Making migrations..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

# Ensure proper permissions
chmod -R 755 staticfiles/
chmod -R 755 media/

echo "Build completed successfully!" 