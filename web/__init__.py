import asyncio
import logging
import logging.config
import os
from types import MappingProxyType

from aiohttp import web
import aiohttp_jinja2
import jinja2

from web.router import configure_handlers, routes
from web.utils.assets import AssetManager
from web.utils.settings import get_config


here = os.path.abspath(__file__)
log = logging.getLogger(__name__)


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

    # static assets
    static_dir = os.path.join(os.path.dirname(here), 'public')
    application.assets = AssetManager(application, prefix='/static', directory=static_dir)
    manifest_file = os.path.join(os.path.dirname(here), 'manifest.json')
    application.assets.load_manifest(manifest_file)

    # templates

    template_dir = os.path.join(os.path.dirname(__file__), 'templates')
    env = aiohttp_jinja2.setup(
        application, loader=jinja2.FileSystemLoader(template_dir)
    )
    env.globals['asset'] = application.assets.get_path

    # connect routes
    configure_handlers(application, routes)

    # shutdown connection clean-up
    async def on_shutdown_close_conns(app):
        if app.connections:
            log.info('Force closing %s open stream connections.', len(app.connections))
            for resp in app.connections:
                resp.should_stop = True

    application.connections = set()
    application.on_shutdown.append(on_shutdown_close_conns)

    return application


here = os.path.abspath(os.path.dirname(__file__))
conf_file = os.path.join(here, '../config/web.yml')
main = build_app(settings_path=conf_file)

