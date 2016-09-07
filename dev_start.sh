#! /bin/bash

npm run build:dev
PORT=5000 ROOT_LOG_LEVEL=DEBUG gunicorn web:main --config config/gunicorn.conf --reload

