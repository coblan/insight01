from base import *
STATICFILES_DIRS = (os.path.join(BASE_DIR,'static'),)

from helpers.maintenance.log import log_setting
log_setting.SET(globals())

#TEMPLATE_DEBUG = True

DEBUG=False
ALLOWED_HOSTS=['i01.enjoyst.com']

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
    ('coblan', 'coblan@163.com'),
)

MANAGERS = (
    ('coblan', 'coblan@163.com'),
)

EMAIL_HOST='smtp.163.com'
EMAIL_HOST_PASSWORD='he7125158'
EMAIL_HOST_USER='coblan'
EMAIL_SUBJECT_PREFIX='[INSIGHT01]'
SERVER_EMAIL='coblan@163.com'
DEFAULT_FROM_EMAIL='coblan@163.com'



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