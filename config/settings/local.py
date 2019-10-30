from .base import *

DEBUG = True

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

THIRD_PARTY_APPS += ['debug_toolbar']

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ALLOWED_HOSTS = INTERNAL_IPS

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


RECAPTCHA_PUBLIC_KEY = '6LfBK8AUAAAAACyWLgnnrJT8wkT5jPqdIQNsRhiU'
RECAPTCHA_PRIVATE_KEY = '6LfBK8AUAAAAALW-8sxX2A07E279JnKg_a5BzCcJ'
