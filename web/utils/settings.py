from tempfile import NamedTemporaryFile
from types import MappingProxyType
import importlib.util
import os.path
import shutil
import sys


def get_config(filename):
    try:
        config_dir = os.path.dirname(filename)

        with NamedTemporaryFile(suffix='.py', dir=config_dir, delete=True) as tf:
            shutil.copyfile(filename, tf.name)
            spec = importlib.util.spec_from_file_location('_config.settings', tf.name)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

        if hasattr(module, '__all__'):
            settings = {k: getattr(module, k) for k in module.__all__}
        else:
            settings = {k: v for k, v in vars(module).items() if not k.startswith('_')}

        return MappingProxyType(settings)

    except Exception:
        sys.stderr.write('Failed to read config file: %s' % filename)
        sys.stderr.flush()
        raise
