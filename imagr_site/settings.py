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

    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/
    # SECURITY WARNING: keep the secret key used in production secret!
    with open('access/secret_key.txt') as f:
        SECRET_KEY = str(f.read().strip())

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True

    TEMPLATE_DEBUG = True

    ALLOWED_HOSTS = ["ec2-54-187-91-202.us-west-2.compute.amazonaws.com"]

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
        # 'OPTIONS': {
        #     'autocommit': True,
        # }
    }

    with open("access/db_secret_key.txt") as f:
        DATABASES["default"]['USER'] = str(f.read().strip())[0]
        DATABASES["default"]['PASSWORD'] = str(f.read().strip())[1]

    # Internationalization
    # https://docs.djangoproject.com/en/1.6/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    STATIC_URL = '/static/'

    MEDIA_URL = '/media/'
    MEDIA_ROOT = BASE_DIR + "/media/"


class Dev(Common):
    u"""
    The in-development settings and the default configuration.
    """
    pass


class Prod(Common):
    u"""
    The in-production settings.
    """
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    SECRET_KEY = values.SecretValue()
    STATIC_ROOT = BASE_DIR + "/static/"

    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    CONN_MAX_AGE = None
    TEMPLATE_LOADERS = (('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
    )),
    )
