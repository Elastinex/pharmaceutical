# -*- coding:utf-8 -*-

"""
Production settings
"""

from .common import *

DEBUG = False
ALLOWED_HOSTS = ['10.0.0.153', 'localhost']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'emholboo',
        'USER': 'emholboo',
        'PASSWORD': '#DiyjoT42u#M',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": "debug.log",
        },
    },
    "loggers": {
        "django": {"handlers": ["file"], "level": "DEBUG", "propagate": True, },
    },
}
