"""
Django settings for instructscience project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.dirname(os.path.dirname(__file__))

try:
    INSTRUCT_ENV = os.environ['INSTRUCT_ENV']
    INSTRUCT_SECRET_KEY = os.environ['INSTRUCT_SECRET_KEY']
    INSTRUCT_DB_NAME = os.environ['INSTRUCT_DB_NAME']
    INSTRUCT_DB_USER = os.environ['INSTRUCT_DB_USER']
    INSTRUCT_DB_PASSWORD = os.environ['INSTRUCT_DB_PASSWORD']
    INSTRUCT_DB_HOST = os.environ['INSTRUCT_DB_HOST']
    INSTRUCT_ALLOWED_HOSTS = os.environ['INSTRUCT_ALLOWED_HOSTS']
    #INSTRUCT_ALLOWED_HOSTS = '127.0.0.1'
except Exception as e:
    print(f"{str(e)}")
    exit()


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# SECURITY WARNING: don't run with debug turned on in production!
if INSTRUCT_ENV == "DEV":
    DEBUG = True
    USE_LESS = True
elif INSTRUCT_ENV == "PROD":
    DYNAMIC = True
    DEBUG = False
    USE_LESS = False
else:
    DEBUG = True
    USE_LESS = False


ALLOWED_HOSTS = [INSTRUCT_ALLOWED_HOSTS]

SECRET_KEY = INSTRUCT_SECRET_KEY



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'filer',
    'ckeditor',
    'import_export',
    'treebeard',
    'easy_thumbnails',
    'el_pagination',
]
INSTALLED_APPS += [
    'assets',
    'home',
    'blog',
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

ROOT_URLCONF = 'instructscience.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'assets', 'templates')],
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

WSGI_APPLICATION = 'instructscience.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'hxxfmhng',
#         'USER': 'hxxfmhng',
#         'PASSWORD': 'An_3OCfa0Ym9-S947GKIYmqDOsi1dSQc',
#         'HOST': 'satao.db.elephantsql.com',
#         'PORT': '5432',
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'dheeraj$isdb',
#         'USER': 'dheeraj',
#         'PASSWORD': 'admin@123',
#         'HOST': 'dheeraj.mysql.pythonanywhere-services.com',
#         'OPTIONS': {
#             'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
#             'charset': 'utf8mb4',
#         }
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': INSTRUCT_DB_NAME,
        'USER': INSTRUCT_DB_USER,
        'PASSWORD': INSTRUCT_DB_PASSWORD,
        'HOST': INSTRUCT_DB_HOST,
        'PORT': '5432',
    }
}

SITE_ID = 1

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
]
# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE =  'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = False

FILE_UPLOAD_PERMISSIONS = 0o644

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, os.path.join(DATA_DIR, 'assets/media'))
STATIC_ROOT = os.path.join(DATA_DIR, os.path.join(DATA_DIR, 'assets/static'))

# Ck - Editor settings
CKEDITOR_CONFIGS = {
    'default': {
        'removePlugins': 'stylesheetparser',
        'allowedContent': True,
        'extraAllowedContent': (
            'div(col-md-*,container-fluid,\
                                row,tabpanel,tab-pane),\
                                *[id], *',
        )
    },
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'science.log'),
            'formatter': 'verbose',
            'maxBytes': 1024 * 1024 * 3,
            'backupCount': 2
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'embassycovid.custom': {
            'handlers': ['file'],
            'level': 'INFO',
        },
    }
}
