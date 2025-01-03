"""
Django settings for vulnconsole project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
import sys
from pathlib import Path
from django.contrib import messages
import dj_database_url

import os
from dotenv import load_dotenv

load_dotenv()  # This will load the environment variables from the .env file


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# os.environ.get("SECRET_KEY") removed the secret key from .env for final project to have simpler functionality
SECRET_KEY = 'django-insecure-cvb)#jt)^00sj)q8-m9=3llp9qh4=++==g0s=v+s@s!bhl3!vc'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = os.environ.get("DEBUG", "False").lower() =="true"
DEBUG = False

# ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(" ")

ALLOWED_HOSTS = ['vulnbyte.onrender.com']

# ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # other
    'crispy_forms',
    # apps
    'vulnscan.apps.VulnscanConfig',
    # 'authentication.apps.AuthenticationConfig',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'vulnconsole.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'vulnconsole.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'vulnbyte',
        'USER': 'postgres1',
        'PASSWORD': '@FINALPROJECT',
        'HOST': 'localhost',  # or 'db' if using docker-compose
        'PORT': '5432',
    }
}

DATABASES["default"] = dj_database_url.parse("postgresql://postgres1:Mefj2k9MWKXHnIWiGOrYsMPROMpIJb7e@dpg-ctlj4152ng1s73b7f4fg-a.oregon-postgres.render.com/vulnbyte")

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.environ.get('DB_NAME'),
#         'USER': os.environ.get('DB_USER'),
#         'PASSWORD': os.environ.get('DB_USER_PASSWORD'),
#         'HOST': os.environ.get('DB_HOST'),
#     }
# }

# DATABASE_URL = os.environ.get("DATABASE_URL")
# DATABASES = {
#     'default': dj_database_url.parse(DATABASE_URL)
# }
# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Chicago'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# Specify the path where static files will be collected
STATIC_ROOT = BASE_DIR / "staticfiles"  # Collect static files here

# Directories where Django will look for static files during development
STATICFILES_DIRS = [
    BASE_DIR / "static",  # Local static files (for development)
]

MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}

# Using a testing email backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# email stuff
# EMAIL_HOST = os.environ.get('EMAIL_HOST')
# EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
# EMAIL_USE_TLS = True
# DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')
# EMAIL_PORT = 587
# EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

# Configuration of output log messages to the console
if (len(sys.argv) >= 2 and sys.argv[1] == 'runserver'):
    print('Running locally')
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
            }
        },
        'loggers': {
            'django.db.backends': {
                'handlers': ['console'],
                'level': 'DEBUG',
            },
        }
    }
