Heroku aiohttp Web Template
===========================

An opinionated project template for deploying an [aiohttp](https://github.com/KeepSafe/aiohttp/)
web app to Heroku, designed to encourage the rapid development and deployment of real-time
front-end features.

**NB:** _This remains a work-in-progress. Please tread carefully._

Launch the app
--------------

Use this button:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com/sseg/heroku-aiohttp-template&template=https%3A%2F%2Fgithub.com/sseg/heroku-aiohttp-template)

Or alternatively:

    $ git clone https://github.com/sseg/heroku-aiohttp-web.git
    $ cd heroku-aiohttp-web
    $ heroku create
    $ heroku buildpacks:set https://github.com/heroku/heroku-buildpack-multi.git
    $ heroku config:set ROOT_LOG_LEVEL=INFO
    $ git push heroku master


Develop locally
---------------

Make sure you have:

- a Python 3.5+ virtual environment ([venv](https://docs.python.org/3/library/venv.html))
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

Local config values are defined in the `.env` file, and invoked when you start
the application using `heroku local`.

### Run the tests

There are no tests yet... but stay tuned!


Application structure
---------------------

#### Handlers

_aiohttp_ dispatches requests to handlers which can be either coroutines or functions
that accept a [Request](http://aiohttp.readthedocs.io/en/stable/web_reference.html#aiohttp.web.Request) and return a [Response](http://aiohttp.readthedocs.io/en/stable/web_reference.html#aiohttp.web.Response). A base class
[aiohttp.web.View](http://aiohttp.readthedocs.io/en/stable/web_reference.html#aiohttp.web.View)
is also provided to help organize handlers into classes, which provides the convenience of
automatically creating an OPTIONS method.  

#### Templates

This app uses [jinja2](http://jinja.pocoo.org/) templates to construct its index
view. Template files are kept in the _web/templates_ directory and compiled by
the [aiohttp_jinja2](https://github.com/aio-libs/aiohttp_jinja2) renderer. You might
prefer [mako](https://github.com/aio-libs/aiohttp_mako) for templates, or
[something](https://wiki.python.org/moin/Templating)
[else](https://docs.python.org/3/library/string.html#template-strings)—connecting
a new renderer to your handlers is easy.

#### Static files

Javascript and CSS source files are defined in the _assets/js_
and _assets/css_ directories, respectively. These assets are compiled by
[brunch](http://brunch.io/) to the top-level _public_ directory (configuration
in _brunch-config.js_). You might want to add React or Elm compilation which is
as simple as installing a new [brunch plugin](http://brunch.io/plugins). In
development you can run a file watcher with an HTTP + pushstate server to reload
your page on file changes (this is started with the *dev_start.sh* script).

#### Production asset delivery

In production the assets are compiled once (triggered during Heroku deployment by
_package.json_'s postinstall directive). Based on the Python configuration the compiled
assets are served through _aiohttp_ (with the piping handled by
_web.utils.assets.AssetManager_).

**NB:** the _aiohttp_ server is not designed to serve static files, and allowing
it to serve production asset traffic will detrimentally affect your application's
performance. You will either want to expose this application behind a content
delivery proxy (e.g. [Cloudflare](https://www.cloudflare.com/)) or reconfigure it
to serve assets from a separate assets server. The _brunch_ asset compiler is
configured here to append checksum digests to asset filenames which facilitates
cache eviction in these scenarios.

#### Configuration

This application uses a configuration base file, _config/web.yml_, which defines
defaults and wraps environment variables. New configuration settings should be added
to this file and refer to new environment variables. For more information on Heroku
app configuration see the [devcenter](https://devcenter.heroku.com/articles/config-vars)
docs.


Contributions
-------------

Contributions are welcome! Bugs, feature requests, and unanswered questions can be
reported in the Github issue tracker [here](https://github.com/sseg/heroku-aiohttp-web/issues).
Fixes, enhancements, and suggestions are also gratefully accepted in pull requests.
