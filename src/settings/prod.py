from base import *
STATICFILES_DIRS = (os.path.join(BASE_DIR,'static'),)

from helpers.maintenance.log import log_setting
log_setting.SET(globals())

TEMPLATE_DEBUG = True


DATABASES = {
    'default': {
        'NAME': 'insight01',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'root',
        'PASSWORD': 'he123811',
        'HOST': '127.0.0.1', 
        'PORT': '3306',        
      },
    }