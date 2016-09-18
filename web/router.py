from collections import namedtuple

from web.handlers import index, tick


Route = namedtuple('Route', ['name', 'method', 'path', 'handler'])

routes = [
    Route('index', 'GET', '/', index),
    Route('tick', 'GET', '/tick', tick)
]


def configure_handlers(app, routing_map, prefix=None):
    for routing in routing_map:
        path = prefix + routing.path if prefix is not None else routing.path
        app.router.add_route(routing.method, path, routing.handler, name=routing.name)
