import os
from pathlib import Path
from django.urls import reverse_lazy

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-9&#dlbycka#1c9kocdq+1j86_jxpnfro+octkl%&k&xio0jx9r'
DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'captcha',

    'dog_walks.places',
    'dog_walks.accounts',
    'dog_walks.common',
]
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379", }
}
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'dog_walks.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'dog_walks.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dog_walks_db',
        'USER': 'postgres-user',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'dog_walks.accounts.validators.MyMinimumLengthValidator',
    },
    {
        'NAME': 'dog_walks.accounts.validators.MyCommonPasswordValidator',
    },
    {
        'NAME': 'dog_walks.accounts.validators.MyNumericPasswordValidator',
    },
]

CSRF_FAILURE_VIEW = 'dog_walks.exception_handlers.csrf_failure'
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = False

USE_TZ = True

DATE_FORMAT = 'd/m/Y'
TIME_FORMAT = 'H:i'
DATETIME_FORMAT = "d/m/Y H:i:s"

STATIC_URL = '/static/'
STATICFILES_DIRS = (BASE_DIR / 'staticfiles',)

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media_files'

LOGIN_URL = reverse_lazy('login user')
LOGIN_REDIRECT_URL = reverse_lazy('index')

AUTH_USER_MODEL = 'accounts.AppUser'
PHONENUMBER_DEFAULT_REGION = 'BG'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

RECAPTCHA_PUBLIC_KEY = '6Ld1i3wjAAAAAEADAr3IPKD7cP6gA6hxyfxObX_2'
RECAPTCHA_PRIVATE_KEY = '6Ld1i3wjAAAAACQ-iNV_MwUaLC2LhUZZB6EuyltT'
