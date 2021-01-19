import os
from pathlib import Path
from environs import Env
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent.parent


def join(path):
    return os.path.join(BASE_DIR, path)


env = Env()
env.read_env(recurse=False, path=join('.env'))

SECRET_KEY = env("SECRET_KEY", "=)lpcfnj$#7$e1==+!9la_0yq8)w79!k_&t^-76i*_+83z2ymy")
DEBUG = env.bool("DEBUG", True)
ALLOWED_HOSTS = env("ALLOWED_HOSTS", ['*'])
DRF_ENABLED = env("DRF_ENABLED", True)
CURRENT_SITE_DOMAIN = env("CURRENT_SITE_DOMAIN", "http://127.0.0.1:8000")


INSTALLED_APPS = [
    # django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',

    # third-party
    'drf_yasg',
    'rest_framework',
    'django_filters',
    'corsheaders',

    # app

]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = '_core.urls'

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

WSGI_APPLICATION = '_core.wsgi.application'

# Database
with env.prefixed('DB_') as e:
    DATABASES = {
        'default': dict(
            ENGINE='django.contrib.gis.db.backends.postgis',
            NAME=e('NAME'),
            USER=e('USER'),
            PASSWORD=e('PASS'),
            HOST=e('HOST'),
            PORT=e('PORT')
        )
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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = join('static')
MEDIA_URL = '/media/'
MEDIA_ROOT = join("media")

# AUTH_USER_MODEL = 'account.CustomUser'

with env.prefixed('CORS_ORIGIN_') as e:
    CORS_ORIGIN_ALLOW_ALL = e.bool('ALLOW_CREDENTIALS', True)
    CORS_ORIGIN_WHITELIST = e.list('WHITELIST', ['localhost'])

ACCESS_TOKEN_LIFETIME = env.int('ACCESS_TOKEN_LIFETIME_DAYS', 1)
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=ACCESS_TOKEN_LIFETIME),
    'REFRESH_TOKEN_LIFETIME': timedelta(weeks=ACCESS_TOKEN_LIFETIME),
    'ROTATE_REFRESH_TOKENS': True,
}

_DEFAULT_TIME_RELATED_FORMAT = "%Y-%m-%d"

REST_FRAMEWORK = dict(
    # DEFAULT_PERMISSION_CLASSES=('rest_framework.permissions.IsAuthenticated',),
    DEFAULT_AUTHENTICATION_CLASSES=('rest_framework_simplejwt.authentication.JWTAuthentication',),
    UNAUTHENTICATED_USER=None,
    DEFAULT_RENDERER_CLASSES=('rest_framework.renderers.JSONRenderer',),
    DEFAULT_PAGINATION_CLASS='utils.paginations.DefaultPagination',
    DATE_FORMAT=_DEFAULT_TIME_RELATED_FORMAT,
    DATE_INPUT_FORMATS=[_DEFAULT_TIME_RELATED_FORMAT],
    DATETIME_FORMAT=_DEFAULT_TIME_RELATED_FORMAT,
    DATETIME_INPUT_FORMATS=[_DEFAULT_TIME_RELATED_FORMAT],
    TIME_FORMAT=_DEFAULT_TIME_RELATED_FORMAT,
    TIME_INPUT_FORMATS=[_DEFAULT_TIME_RELATED_FORMAT]
)

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    },
    'JSON_EDITOR': True,
    'VALIDATOR_URL': None,
    'SHOW_REQUEST_HEADERS': False,
    'APIS_SORTER': 'alpha',
    'DEEP_LINKING': True,
    'USE_SESSION_AUTH': False,
    'REFETCH_SCHEMA_WITH_AUTH': True,
    'PERSIST_AUTH': False,
    'DEFAULT_MODEL_RENDERING': 'example',
    'DOC_EXPANSION': 'none',
    'DEFAULT_FIELD_INSPECTORS': (
        'drf_yasg.inspectors.CamelCaseJSONFilter',
        'drf_yasg.inspectors.RecursiveFieldInspector',
        'drf_yasg.inspectors.ReferencingSerializerInspector',
        'drf_yasg.inspectors.ChoiceFieldInspector',
        'drf_yasg.inspectors.FileFieldInspector',
        'drf_yasg.inspectors.DictFieldInspector',
        'drf_yasg.inspectors.HiddenFieldInspector',
        'drf_yasg.inspectors.RelatedFieldInspector',
        'drf_yasg.inspectors.SerializerMethodFieldInspector',
        'drf_yasg.inspectors.SimpleFieldInspector',
        'drf_yasg.inspectors.StringDefaultFieldInspector',
    )
}
