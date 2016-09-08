#! /bin/bash

brunch w -s -d &
PORT=5000 ENV=DEVELOPMENT gunicorn web:main --config config/gunicorn.conf --reload

