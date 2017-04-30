from base import *
STATICFILES_DIRS = (os.path.join(BASE_DIR,'static'),)

from log import *
MIDDLEWARE_CLASSES =['helpers.maintenance.request_log.RequestMiddleware']+MIDDLEWARE_CLASSES 

TEMPLATE_DEBUG = True


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