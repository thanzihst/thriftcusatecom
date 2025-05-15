#!/bin/bash

# Exit on error
set -e

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Creating static directory if it doesn't exist..."
mkdir -p staticfiles

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Creating api directory if it doesn't exist..."
mkdir -p api

echo "Making migrations..."
python manage.py makemigrations
python manage.py migrate

echo "Build completed successfully!" 