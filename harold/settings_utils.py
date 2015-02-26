import os


NO_VALUE = object()


def parse_identity(val):
    return val


def parse_bool(val):
    true_vals = ('t', 'true', 'yes', 'y')
    false_vals = ('f', 'false', 'no', 'n')

    val = val.lower()
    if val in true_vals:
        return True
    if val in false_vals:
        return False

    raise ValueError('%s is not a valid bool value' % val)


def parse_integer(val):
    return int(val)


def parse_float(val):
    return float(val)


class ConfigurationError(Exception):
    pass


def config(envvar, override_value=NO_VALUE, default=NO_VALUE, type_='str'):
    types = {
        'str': parse_identity,
        'int': parse_integer,
        'float': parse_float
    }

    # Prefer the override if there is one
    if override_value is not NO_VALUE:
        return override_value

    # Check the environment
    val = os.environ.get(envvar, NO_VALUE)
    if val is not NO_VALUE:
        return types[type_](val)

    # Try the default
    if default is not NO_VALUE:
        return default

    raise ConfigurationError('%s requires a value of type %s' % (envvar, type_))
