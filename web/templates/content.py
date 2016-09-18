from markdown import markdown
from functools import lru_cache


index = {
    "what_is_this": """

This application is a starter template for building real-time web apps. It's running on a
Python [aiohttp]("http://aiohttp.readthedocs.io/") server. The above "Server Ticks"
timestamps are sent from the server and subscribed to using the
[EventSource]("https://developer.mozilla.org/en/docs/Web/API/EventSource") API.

`aiohttp` is an asynchronous web framework that exposes client and server APIs
letting you easily develop HTTP applications with persistent connections. It runs
on the `asyncio` event loop which encourages clean, readable code (no threads, no callbacks).
Its features include:

- pluggable routing and middlewares
- websockets
- file upload support
- a growing library of tools: [aio-libs](https://github.com/aio-libs/)

    """,

    "where_next": """

If you deployed this app using the "Deploy to Heroku" button you'll want to
install a local copy:

    $ git clone https://github.com/sseg/heroku-aiohttp-web.git
    $ cd heroku-aiohttp-web
    $ heroku git:remote -a <your-app-name>

Follow the instructions for setting up a local environment in the project
[readme](https://github.com/sseg/heroku-aiohttp-web/blob/master/README.md). There
you can read more about the project struture, dependencies, and deployment guidelines.

    """,

    "alert_guide": """

If you're not familiar with the Heroku platform you may want to start with their excellent
[Python getting started guide](https://devcenter.heroku.com/articles/getting-started-with-python).

    """,

    "helpful_links": """

- [Project Source](https://github.com/sseg/heroku-aiohttp-web)

##### aiohttp and asyncio
- [aiohttp Documentation](http://aiohttp.readthedocs.io/en/stable/)
- [Develop with asyncio](https://docs.python.org/3/library/asyncio-dev.html)
- [asyncio-based Libraries](https://github.com/aio-libs/)

##### Heroku
- [Heroku Getting Started guides](https://devcenter.heroku.com/start)
- [Heroku Architecture](https://devcenter.heroku.com/categories/heroku-architecture)
- [CLI tools](https://toolbelt.heroku.com)

    """
}


source = {
    'index': index
}


@lru_cache(maxsize=None)
def get_content(*path):
    md = source
    for key in path:
        md = md[key]
    return markdown(md)
