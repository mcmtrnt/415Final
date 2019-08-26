"""
Django settings for scraper project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import shutil
import stripe

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# os.environ["PYTHONIOENCODING"] = "utf-8"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'cet9t4*(7o7ss%crq)%_3f(%p^^!)!&=$_a1w2olijy=n(+m87'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.0', '18.222.138.188', '127.0.0.1']

STRIPE_PUBLIC_KEY = "pk_test_CNCYl3Rg3Tfg0QbgsyL9wTAg00kCZhOvs5"
STRIPE_SECRET_KEY = "sk_test_KRTXzuhlafgFkjyxb2zDIGGw00ScFtCMAa"
stripe.api_key = STRIPE_SECRET_KEY

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_mako_plus',
    'homepage',
]

# CRON_CLASSES = [
#     "homepage.cron.MyCronJob",
#     # ...
# ]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django_mako_plus.RequestInitMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'scraper.urls'

TEMPLATES = [
    {
        'NAME': 'django_mako_plus',
        'BACKEND': 'django_mako_plus.MakoTemplates',
        'OPTIONS': {
            # see the DMP documentation, "configuration options" page for available options
        },
    },
    {
        'NAME': 'django',
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'scraper.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'ksl',
#         'USER': 'postgres',
#         'PASSWORD': 'Chocolate1',
#         'HOST': 'localhost',
#         'PORT': '',
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dirtbikedeals',
        'USER': 'postgres',
        'PASSWORD': 'PASSWORD',
        'HOST': 'database-1.c6tvlnpvgqmk.us-east-2.rds.amazonaws.com',
        'PORT': '5432',
    }
}




# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    # SECURITY WARNING: this next line must be commented out at deployment
    BASE_DIR,
)
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


# A logger for DMP
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'django_mako_plus_simple': {
            'format': '%(levelname)s::DMP %(message)s'
        },
    },
    'handlers': {
        'django_mako_plus_console':{
            'class':'logging.StreamHandler',
            'formatter': 'django_mako_plus_simple'
        },
    },
    'loggers': {
        'django_mako_plus': {
            'handlers': ['django_mako_plus_console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}
