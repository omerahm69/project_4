
from pathlib import Path
import os
import django_heroku
import dj_database_url
if os.path.isfile('env.py'):
    import env
import os
from dotenv import load_dotenv
# cloudinary import
import cloudinary
import cloudinary_storage
import cloudinary.uploader
import cloudinary.api
from django.core.files.storage import default_storage

# Load .env file
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join( BASE_DIR , 'templates')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('django-insecure-!+oz1)35@#_90iyon!k4d98++mi@92x5%8#_qfeuo5_2%!=t&%')

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = os.getenv('DEBUG', 'False') == 'True'


ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '127.0.0.1,.herokuapp.com').split(',')



# Application definition

INSTALLED_APPS = [
    
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.auth',
    'allauth',
    'allauth.account',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary_storage',
    'cloudinary',
    'my_restaurant.apps.MyRestaurantConfig',
    
]

SITE_ID = 1
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'restaurant.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
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

WSGI_APPLICATION = 'restaurant.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'aloha_kite_patch_309821',
        'USER': 'neondb_owner',
        'PASSWORD': 'RjCNAK0qS8Iy',
        'HOST': 'ep-orange-bush-a29x4sqc.eu-central-1.aws.neon.tech',
        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

ACCOUNT_EMAIL_VERIFICATION = 'none'
# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATIC_URL = '/static/'


MEDIA_URL = 'media/'
MEDIA_ROOT=BASE_DIR / 'uploads/'

if 'DYNO' in os.environ:
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

if 'DYNO' in os.environ:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True


DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"


django_heroku.settings(locals())

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.getenv('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': os.getenv('CLOUDINARY_API_KEY'),
    'API_SECRET': os.getenv('CLOUDINARY_API_SECRET'),
}

# Cloudinary configuration
cloudinary.config(
    cloud_name=os.getenv('CLOUDINARY_CLOUD_NAME'),
    api_key=os.getenv('CLOUDINARY_API_KEY'),
    api_secret=os.getenv('CLOUDINARY_API_SECRET'),
)
