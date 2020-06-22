from django.conf import settings
import os


INSTALLED_APPS = settings.INSTALLED_APPS + ['debug_toolbar',]
MIDDLEWARE = settings.MIDDLEWARE +['debug_toolbar.middleware.DebugToolbarMiddleware',]
INTERNAL_IPS = [
    '127.0.0.1',
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
            'propagate': False,
        },
    },
}