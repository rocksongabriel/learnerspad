from .base import *

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'learnerspad_testing_db',
        'USER': 'rocksongabriel',
        'PASSWORD': 'iamthedarkbotBORNin1999',
        'HOST': 'localhost',
        'PORT': 5432
    }
}