from pathlib import Path
import os
from dotenv import load_dotenv
load_dotenv()

# Environment variable
SECRET_KEY = os.getenv("djnago_sec_key")
DEBUG = True

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "website_app",
    "product",
    "booking",
    "contact",
    "about_us",
    "payment",
    'django_filters',
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

ROOT_URLCONF = 'tourist.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "template")],
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

WSGI_APPLICATION = 'tourist.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv("DB_name"),
        'USER': os.getenv("DB_user"),
        'PASSWORD': os.getenv("DB_passwd"),
        'HOST': os.getenv("DB_host"),
        'PORT': os.getenv("DB_port"),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Local Storage for Static and Media files

# Static files settings
STATIC_URL = '/static/'  # Static URL
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]  # Development directory for static files
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Directory to collect static files

# Media files settings
MEDIA_URL = '/media/'  # Media URL
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Local media directory

# Razorpay keys
RAZORPAY_SECRET_KEY = os.getenv("razor_sec_key")
RAZORPAY_PRODUCT_ID = os.getenv("razor_prod_id")
