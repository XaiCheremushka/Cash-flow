
from pathlib import Path

from config import conf

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = conf.SECRET_KEY.get_secret_value()

DEBUG = True

ALLOWED_HOSTS = conf.ALLOWED_HOSTS.get_secret_value().split(' ')  # ['127.0.0.1', 'localhost']

SITE_URL = f'http://{conf.SITE_HOST}'

SESSION_COOKIE_SECURE = False  # True только для HTTPS!
CSRF_COOKIE_SECURE = False  # True только для HTTPS!


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'cashflow.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'cashflow.wsgi.application'


# -------------------------------- Internationalization -------------------------------------------


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# --------------------------------------- Database -------------------------------------------------------


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': conf.DATABASE_NAME,
        'USER': conf.DATABASE_USER,
        'PASSWORD': conf.DATABASE_PASSWORD.get_secret_value(),
        'HOST': conf.DATABASE_HOST,
        'PORT': conf.DATABASE_PORT,
    }
}


# ------------------------------------ Static --------------------------------------------------------

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Папка, куда будут собираться статические файлы
# Для разработки
if DEBUG:
    STATICFILES_DIRS = [
        BASE_DIR / 'static'
    ]

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'


# ------------------------------------- Authentication ------------------------------------------------


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
