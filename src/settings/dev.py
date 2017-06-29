from base import *
from helpers.debug.debug_toolbar import debugtoolbar_setting

#debugtoolbar_setting.SET(globals())

STATICFILES_DIRS = (os.path.join(BASE_DIR,'static'),)

from helpers.maintenance.log import log_setting
log_setting.SET(globals())

TEMPLATE_DEBUG = True


import os
if os.environ.get('TEST'):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db.sqlite3',
        }
    }  
else:
    DATABASES = {
        'default': {
            'NAME': 'insight01',
            'ENGINE': 'django.db.backends.mysql',
            'USER': 'root',
            'PASSWORD': 'root',
            'HOST': '127.0.0.1', 
            'PORT': '3306',        
          },
        }

