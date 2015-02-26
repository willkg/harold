from harold.settings_utils import config, NO_VALUE

# Instance settings that are required
SECRET_KEY = NO_VALUE
BROWSERID_AUDIENCES = NO_VALUE
DATABASES = NO_VALUE

# Pull in the default settings
from harold.settings.defaults import *

# Override with local.py
try:
    from harold.settings.local import *
except ImportError:
    pass


# Instance settings which should come from the environment but can
# come from local.py.

import dj_database_url

SECRET_KEY = config(
    'SECRET_KEY', override_value=SECRET_KEY, type_='str')
# FIXME: This should be a list of strings
BROWSERID_AUDIENCES = [
    config(
        'BROWSERID_AUDIENCES', override_value=SITE_URL, default='http://127.0.0.1:8000', type_='str')
]
# FIXME: Gross.
ADMINS = [
    admin for admin in [
        config('ADMINS', override_value=ADMINS, default=None, type_='str')
    ]
]

if DATABASES is NO_VALUE:
    DATABASES = {
        'default': dj_database_url.config(default='sqlite:///harold.db')
    }
