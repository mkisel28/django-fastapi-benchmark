"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 5.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-nt_9u*_%n4$x)e^r72##$^11s_2hxtrurmcr&mf@q9j*i@9!p*"

DEBUG = False

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    'app',
]

ROOT_URLCONF = "config.urls"

ASGI_APPLICATION = "config.asgi.application"
WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "db",
        "PORT": 5432,
        "OPTIONS": {
            "pool": {
                "min_size": 5,  # Минимальное число соединений
                "max_size": 20,  # Максимальное число соединений в пуле
                "timeout": 10,   # Тайм-аут ожидания свободного соединения
            },
            "server_side_binding": True,  # Включить серверный курсор (оптимизация больших запросов)
        },
    },
}


LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
