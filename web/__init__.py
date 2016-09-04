import asyncio
import logging
import logging.config
import os
from types import MappingProxyType

from aiohttp import web

from web.utils.settings import get_config


def build_app(settings_path, loop=None):
    settings = get_config(settings_path)

    logging.config.dictConfig(settings['logging'])

    loop = loop or asyncio.get_event_loop()

    aio_debug = settings.get('asyncio_debug_enabled', False)
    if aio_debug is True:
        loop.set_debug(True)

    middlewares = [

    ]

    application = web.Application(
        loop=loop,
        middlewares=middlewares
    )

    application.settings = MappingProxyType(settings)

    return application


here = os.path.abspath(os.path.dirname(__file__))
conf_file = os.path.join(here, '../config/web.yml')
main = build_app(settings_path=conf_file)

