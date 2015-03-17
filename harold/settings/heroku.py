# Appropriate for running on Heroku
from harold.settings.base import *
from harold.settings_utils import config, NO_VALUE

DEBUG = TEMPLATE_DEBUG = False

# Mailgun configuration.
if 'MAILGUN_API_KEY' in os.environ:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

    EMAIL_HOST = config('MAILGUN_SMTP_SERVER', type_='str')
    EMAIL_PORT = config('MAILGUN_SMTP_PORT', type_='int')
    EMAIL_USE_TLS = EMAIL_PORT == 587
    EMAIL_HOST_USER = config('MAILGUN_SMTP_LOGIN', type_='str')
    EMAIL_HOST_PASSWORD = config('MAILGUN_SMTP_PASSWORD', type_='str')
    EMAIL_SUBJECT_PREFIX = config('EMAIL_SUBJECT_PREFIX', default='[harold] ', type_='str')
    DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL', type_='str')
