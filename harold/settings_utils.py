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


def config(envvar, default=NO_VALUE, type_='str'):
    types = {
        'str': parse_identity,
        'int': parse_integer,
        'float': parse_float,
        'bool': parse_bool
    }

    # Check the environment for the specified variable and use that
    val = os.environ.get(envvar, NO_VALUE)
    if val is not NO_VALUE:
        return types[type_](val)

    # If there's a default, use that
    if default is not NO_VALUE:
        return default

    # No value specified and no default, so raise an error to the user
    raise ConfigurationError('%s requires a value of type %s' % (envvar, type_))
