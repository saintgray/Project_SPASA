
from pathlib import Path
import os
from .router import TEMPLATE_ROUTERS
from .router import MODULES_ROUTERS
from .router import BASE_DIR

BASE_DIR = Path(__file__).resolve().parent.parent

ROOT_URLCONF = 'app.urls'

ALLOWED_HOSTS = ['localhost', '__local_ip__', '__external__ip__']

DEBUG = True

SECRET_KEY = '__secret_key__'

WSGI_APPLICATION = 'app.wsgi.application'

STATIC_URL = 'static/'

STATIC_DIR=os.path.join(BASE_DIR / 'app', 'static')

STATICFILES_DIRS=MODULES_ROUTERS + TEMPLATE_ROUTERS + [STATIC_DIR]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # My App modules
    'module_entity',
    'view'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # request pre-handle support
    'authentication.pre_handle_request',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS':TEMPLATE_ROUTERS,
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

DATABASES = {
    'default': {
        'ENGINE': '__db_engine__',
        'NAME': '__tnsname__',
        'USER': '__schema__',
        'PASSWORD': '__password__',
        'HOST': '__host__',
        'PORT': '__port__',
    }
}

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

LANGUAGE_CODE = 'ko-KR'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


