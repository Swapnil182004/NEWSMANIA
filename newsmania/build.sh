#!/bin/bash

# Exit if any command fails
set -o errexit  

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt  

# Collect static files
python manage.py collectstatic --noinput  

# Run database migrations
python manage.py migrate  
