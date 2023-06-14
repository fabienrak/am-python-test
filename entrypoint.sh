#!/bin/sh
exec gunicorn --config src/gunicorn.py wsgi:api_app