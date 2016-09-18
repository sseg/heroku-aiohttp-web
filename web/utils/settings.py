from os.path import expandvars
import yaml


def expand_nested_vars(mapping):
    new = {}
    for k, v in mapping.items():
        if hasattr(v, 'items'):
            new[k] = expand_nested_vars(v)
        elif isinstance(v, str):
            new[k] = expandvars(v)
        elif hasattr(v, '__iter__'):
            new[k] = type(v)(expandvars(i) if isinstance(i, str) else i for i in v)
        else:
            new[k] = v
    return new


def get_config(filename):
    with open(filename) as fp:
        base = yaml.safe_load(fp.read())
    return expand_nested_vars(base)
