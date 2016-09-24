logging = {
    'version': 1,
    'formatters': {
        'detail': {
            'format': '{asctime} {levelname:5.5} [{process}] [{name}] [{threadName}] {message}',
            'style': '{'
        },
        'simple': {}
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'detail',
            'stream': 'ext://sys.stdout'
        }
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['console']
    },
    'loggers': {
        'asyncio': {},
        'aiohttp': {},
        'gunicorn': {},
        'web': {}
    }
}

asyncio_debug_enabled = True

assets = {
    'manifest': 'manifest.json.dev',
    'base_path': 'http://0.0.0.0:9484',
    'use_proxy': True
}
