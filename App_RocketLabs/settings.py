# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
Django settings for App_RocketLabs project.

Generated by 'django-admin startproject' using Django 1.11.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""


import os
import os.path
#from decouple import config
from django.contrib.messages import constants as message_constants

MESSAGE_LEVEL = message_constants.DEBUG

# Messages class tags. Definen el color de los diferentes tipos de mensajes.
MESSAGE_TAGS = {
    message_constants.DEBUG: 'w3-light-gray w3-border-black w3-text-dark-gray',
    message_constants.INFO: 'w3-pale-blue w3-border-blue w3-text-blue',
    message_constants.SUCCESS: 'w3-pale-green w3-border-green w3-text-green ',
    message_constants.WARNING: 'w3-sand w3-border-orange w3-text-orange',
    message_constants.ERROR: 'w3-pale-red w3-border-red w3-text-red',
}


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&@np^x6zh6ar7wn)m-)&^kg576#5&-p&wjq9b-y$^hhrdt&24n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ["*"]



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core_app',
    'bundles_app',
    'projects_app',
    'social_django',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'social_django.middleware.SocialAuthExceptionMiddleware', # Redes sociales
]

ROOT_URLCONF = 'App_RocketLabs.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'social_django.context_processors.backends',  # <--
                'social_django.context_processors.login_redirect', # <--
            ],
        },
    },
]

WSGI_APPLICATION = 'App_RocketLabs.wsgi.application'

AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.google.GoogleOAuth2',

    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.social_auth.associate_by_email',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)

#Estas lineas son para tomar el email de facebook
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id,name,email',
}
# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
"""
DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ["DB_NAME"],
        'USER': os.environ["DB_USER"],
        'PASSWORD': os.environ["DB_PASSWORD"],
        'HOST':os.environ["DB_HOST"],
        'PORT':''
    }
}
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

#DATABASES = { 'default': dj_database_url.config() }

#SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Caracas'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = "/home/osvanicolina/App_RocketLabs/core_app/static"

# Configuracion de la carpeta raiz de media en la que se guardaran los
# archivos subidos por los usuarios(Fotos, screenshots, etc)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media' )
MEDIA_URL = '/media/'

# Configuracion para el inicio de sesión desde Redes sociales
# Facebook y Google+

LOGIN_URL = 'core_app:login'
LOGOUT_URL = 'core_app:logout'
LOGIN_REDIRECT_URL = 'core_app:home'

SOCIAL_AUTH_FACEBOOK_KEY = os.environ["SA_FBKEY"]  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = os.environ["SA_FBSECRET"]  # App Secret
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.environ["SA_GPKEY"]
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.environ["SA_GPSECRET"]

# Configuración para el envio de correos desde nuestra plataforma
# Desde un correo gmail.com

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ["HOST_USER"]
EMAIL_HOST_PASSWORD = os.environ["HOST_PASSWORD"]
