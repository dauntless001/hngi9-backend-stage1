from hngApi.settings.base import *
import dj_database_url, os
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG')

MIDDLEWARE.insert(2, "whitenoise.middleware.WhiteNoiseMiddleware")
# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES["default"] = dj_database_url.parse(
    os.getenv("DATABASE_URL"), conn_max_age=600
)

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static'
STATICFILES_DIRS = [

]
