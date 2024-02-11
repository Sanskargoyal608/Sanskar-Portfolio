#!/bin/bash

# Install dependencies from requirements.txt
pip install --no-cache-dir -r requirements.txt

# Collect static files
python3.9 manage.py collectstatic --noinput
