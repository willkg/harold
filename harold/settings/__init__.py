from harold.settings_utils import config, NO_VALUE

# Instance settings that are required
SECRET_KEY = NO_VALUE
SITE_URL = NO_VALUE
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

SECRET_KEY = config('SECRET_KEY', override_value=SECRET_KEY, type_='str')
SITE_URL = config('SITE_URL', override_value=SITE_URL, default='http://127.0.0.1:8000', type_='str')

if DATABASES is NO_VALUE:
    DATABASES = {
        'default': dj_database_url.config(default='sqlite:///harold.db')
    }
