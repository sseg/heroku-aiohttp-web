from json import loads


class AssetManager:
    def __init__(self, app, prefix, directory):
        self.app_router = app.router
        if not prefix.endswith('/'):
            prefix += '/'
        self.prefix = prefix
        self.dir = directory
        self._manifest = None
        self.app_router.add_static(prefix, directory)

    def load_manifest(self, path):
        with open(path) as fp:
            data = loads(fp.read())
        self._manifest = data

    @property
    def manifest(self):
        if self._manifest is None:
            raise RuntimeError('No manifest has been loaded')
        return self._manifest

    def get_path(self, key):
        return self.prefix + self.manifest[key]

