Heroku aiohttp Web Template
===========================

!!! THIS IS A WORK IN PROGRESS !!! TREAD CAREFULLY !!!

An opinionated project template for deploying an [aiohttp](https://github.com/KeepSafe/aiohttp/) web app to Heroku.


Deploy
------

Use this button:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com/sseg/heroku-aiohttp-template&template=https%3A%2F%2Fgithub.com/sseg/heroku-aiohttp-template)

Or alternatively:

    $ git clone git@github.com:sseg/heroku-aiohttp-template.git
    $ cd heroku-aiohttp-template
    $ heroku create
    $ heroku buildpacks:set https://github.com/heroku/heroku-buildpack-multi.git
    $ heroku config:set ROOT_LOG_LEVEL=INFO
    $ git push heroku master


### Static Files

TODO: write a warning about static file delivery



Develop Locally
---------------

Make sure you have:

- a Python 3.5+ virtual environment [venv](https://docs.python.org/3/library/venv.html)
- [node](https://nodejs.org/en/) version 4.5+ with `npm`
- the Heroku CLI tools [Heroku Toolbelt](https://toolbelt.heroku.com)

Install the project packages:

    $ pip install -r dev-requirements.txt
    $ pip-sync
    $ npm install -g brunch
    $ npm install

Then run the project with development asset server:

    $ chmod +x ./dev_start.sh `# run this just once`
    $ ./dev_start.sh

Or run the app using compiled assets with the Procfile:

    $ npm run clean && npm run build:prod
    $ heroku local

Local config values are defined in the `.env` file, and invoked when you start the application using `heroku local`.
