from .base import *

DEBUG = env("DEBUG")

SECRET_KEY = env("SECRET_KEY")

DATABASES = {
    'default': {
        'ENGINE': env("DATABASE_ENGINE"),
        'NAME': env("TEST_DATABASE_NAME"),
        'USER': env("DATABASE_USER"),
        'PASSWORD': env("DATABASE_PASSWORD"),
        'HOST': env("DATABASE_HOST"),
        'PORT': env("DATABASE_PORT")
    }
}