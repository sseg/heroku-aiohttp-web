Heroku aiohttp Starter Template
===============================

!!! THIS IS A WORK IN PROGRESS !!! TREAD CAREFULLY !!!

A project starter template for deploying an [aiohttp](https://github.com/KeepSafe/aiohttp/) app to Heroku.


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


### Config

This app requires that the following environment variables be [set for deployment](https://devcenter.heroku.com/articles/config-vars#setting-up-config-vars-for-a-deployed-application):
- `ROOT_LOG_LEVEL`: one of (`CRITICAL`, `ERROR`, `WARNING`, `INFO`, `DEBUG`)


### Static Files

TODO: write a warning about static file delivery


Develop Locally
---------------

Local config values are defined in the `.env` file, and invoked when you start the application using `heroku local`.

