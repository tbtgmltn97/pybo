from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pybo',
        'USER' : 'encore',
        'PASSWORD' : 'encore!@#',
        'HOST' : '3.38.101.98',
        'PORT' : '3306'
    }
}


