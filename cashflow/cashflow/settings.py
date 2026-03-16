
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

    'drf_spectacular',
    'drf_spectacular_sidecar',  # (необязательно, для красивого UI)

    'rest_framework',

    'rangefilter',

    # Созданные приложения
    'finance',
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


LANGUAGE_CODE = 'ru'

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


# ---------------------------------------------- API ------------------------------------------------------


REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',

    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),

    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
        'rest_framework.throttling.ScopedRateThrottle',
    ],

    'DEFAULT_THROTTLE_RATES': {
        'anon': '20/minute',
        'user': '40/minute',
        'burst': '10/second',
    }

}


# ---------------------------------------- Docs API ----------------------------------------------------


SPECTACULAR_SETTINGS = {
    'TITLE': 'API документация CashFlow',
    'DESCRIPTION': 'Документация для API CashFlow',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    "TAGS": [
        {"name": "ДДС", "description": "Операции с данными для ДДС"},
    ],
}


# ------------------------------------- Logging -------------------------------------------------------------

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,  # Существующие логгеры (например, из сторонних библиотек) продолжат работать.
    'formatters': {
        # Подробный формат (для разработки)
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
        # Короткий формат
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
        # Стандартный формат (для production)
        "standard": {
            "format": "[{asctime}] {levelname} {name}: {message}",
            "style": "{",
        },
    },
    'handlers': {
        'console': {
            # 'level': 'INFO',
            # 'level': 'DEBUG',  # На время разработки
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',  # Логирует от INFO и выше (INFO, WARNING, ERROR, CRITICAL)
            'propagate': False,  # Разрешает передачу логов родительским логгерам (есть неявный родительский логгер)
        },
        # Для разработки, чтобы видеть все SQL-запросы
        # 'django.db.backends': {
        #     'handlers': ['console'],
        #     'level': 'DEBUG',
        # },
        "django.request": {
            "handlers": ["console"],
            "level": "ERROR",
            "propagate": False,
        },
        'cashflow': {
            'handlers': ['console'],
            'level': 'DEBUG',  # Логирует ВСЁ
            'propagate': False,  # Запрещает передачу логов родительским логгерам
        },
    },
}
