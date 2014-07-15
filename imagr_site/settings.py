from configurations import Configuration, values
import os


class Common(Configuration):
    u"""
    Django settings for imagr_site project.

    For more information on this file, see
    https://docs.djangoproject.com/en/1.6/topics/settings/

    For the full list of settings and their values, see
    https://docs.djangoproject.com/en/1.6/ref/settings/
    """
    DEBUG = True

    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    TEMPLATE_DEBUG = True

    ALLOWED_HOSTS = []

    AUTH_USER_MODEL = 'imagr_users.ImagrUser'

    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'easy_thumbnails',
        'imagr_images',
        'imagr_users',
    )

    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

    ROOT_URLCONF = 'imagr_site.urls'

    WSGI_APPLICATION = 'imagr_site.wsgi.application'

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'django_imagr',
            'USER': '',
            'PASSWORD': '',
            'HOST': ''
        },
    }


    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    STATIC_URL = '/imagr_images/static/'
    STATIC_ROOT = BASE_DIR + "imagr_images/static/imagr_images"

    MEDIA_URL = '/media/'
    MEDIA_ROOT = BASE_DIR + "/media/"


class Dev(Common):
    u"""
    The in-development settings and the default configuration.
    """
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    with open(BASE_DIR + '/imagr_site/access/secret_key.txt', 'rb') as f:
        SECRET_KEY = str(f.read().strip())
    yes = "yes"


class Prod(Common):
    u"""
    The in-production settings.
    """
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    with open(BASE_DIR+ '/imagr_site/access/secret_key.txt', 'rb') as f:
        SECRET_KEY = str(f.read().strip())

    #SECRET_KEY = values.SecretValue()
    STATIC_ROOT = os.path.join(BASE_DIR, "/imagr_images/static/")

    ALLOWED_HOSTS = [".ec2-54-191-119-156.us-west-2.compute.amazonaws.com"]

    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    CONN_MAX_AGE = None
    # TEMPLATE_LOADERS = (('django.template.loaders.cached.Loader', (
    #     'django.template.loaders.filesystem.Loader',
    # )),
    # )

    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

    DEBUG = False

    with open("/home/ubuntu/cfpydev-imagr/imagr_site/access/db_secret_key.txt") as f:
        db_user = str(f.readline().strip())
        db_pass = str(f.readline().strip())

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'django_imagr',
            'USER': db_user,
            'PASSWORD': db_pass,
            'HOST': ''
        },
    }

