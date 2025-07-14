#!/bin/bash
cd backend
gunicorn myfirstproject.wsgi:application --bind=0.0.0.0 --timeout 600
