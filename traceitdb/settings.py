"""
Django settings for traceitdb project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-g4-g65#otu)9e!0egsovo00ui=f0aetkvsi1afb2bj84y0xxx5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = (os.environ.get('DJANGO_DEBUG') == "True")

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'rest_framework_simplejwt.token_blacklist',
    'accounts.apps.AccountsConfig',
    'main.apps.MainConfig',
    'researchs.apps.ResearchsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'traceitdb.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'traceitdb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': os.environ['POSTGRES_AUTH_HOST'],
        'PORT': os.environ['POSTGRES_AUTH_PORT'],
        'NAME': os.environ['POSTGRES_AUTH_DB'],
        'USER': os.environ['POSTGRES_AUTH_USER'],
        'PASSWORD': os.environ['POSTGRES_AUTH_PASSWORD'],
        'OPTIONS': {} if DEBUG else {
            'sslmode': 'verify-ca',
            'sslcert': os.environ['POSTGRES_AUTH_SSL_CERT'],
            'sslkey': os.environ['POSTGRES_AUTH_SSL_KEY'],
            'sslrootcert': os.environ['POSTGRES_AUTH_SSL_ROOT_CERT'],
        },
    },
    'main_db': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': os.environ['POSTGRES_HOST'],
        'PORT': os.environ['POSTGRES_PORT'],
        'NAME': os.environ['POSTGRES_DB'],
        'USER': os.environ['POSTGRES_USER'],
        'PASSWORD': os.environ['POSTGRES_PASSWORD'],
        'OPTIONS': {} if DEBUG else {
            'sslmode': 'verify-ca',
            'sslcert': os.environ['POSTGRES_SSL_CERT'],
            'sslkey': os.environ['POSTGRES_SSL_KEY'],
            'sslrootcert': os.environ['POSTGRES_SSL_ROOT_CERT'],
        },
    },
    'researchs_db': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': os.environ['POSTGRES_RESEARCH_HOST'],
        'PORT': os.environ['POSTGRES_RESEARCH_PORT'],
        'NAME': os.environ['POSTGRES_RESEARCH_DB'],
        'USER': os.environ['POSTGRES_RESEARCH_USER'],
        'PASSWORD': os.environ['POSTGRES_RESEARCH_PASSWORD'],
        'OPTIONS': {} if DEBUG else {
            'sslmode': 'verify-ca',
            'sslcert': os.environ['POSTGRES_RESEARCH_SSL_CERT'],
            'sslkey': os.environ['POSTGRES_RESEARCH_SSL_KEY'],
            'sslrootcert': os.environ['POSTGRES_RESEARCH_SSL_ROOT_CERT'],
        },
    }
}

#'database_routers.main.MainRouter'
DATABASE_ROUTERS = ['database_routers.default.DefaultRouter','database_routers.main.MainRouter','database_routers.researchs.ResearchsRouter']

# DEFAULT USER MODEL
AUTH_USER_MODEL = 'accounts.AuthUser'

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# REST FRAMEWORK
REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'accounts.exceptions.core_exception_handler',
    'NON_FIELD_ERRORS_KEY': 'error',
    'DEFAULT_AUTHENTICATION_CLASSES': ('accounts.authentication.TwoFactorAuthentication',),
}

# Simple JWT Settings
# See https://django-rest-framework-simplejwt.readthedocs.io/en/latest/settings.html
SIMPLE_JWT = {
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True
}
