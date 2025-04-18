"""
Django settings for QueryBaseAI.
"""

from pathlib import Path
from dotenv import load_dotenv
from Constant.LLM import LLMProvider

load_dotenv()


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-$g+-33&x37(p$rypvmaw*+u+()z!oo!^_t2pxp)_&cd^ge=ge*"


DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "QueryBaseAI.middleware.LogstashLoggingMiddleware",
]

ROOT_URLCONF = "QueryBaseAI.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "QueryBaseAI.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


STATIC_URL = "static/"


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


ELASTIC_HOST = "localhost"
ELASTIC_PORT = 9200
ELASTIC_HEADER = {"Content-Type": "application/json"}

LOGSTASH_HOST = "localhost"
LOGSTASH_PORT = 5000

MILVUS_HOST = "localhost"
MILVUS_PORT = 19530

VECTOR_DIMENSION = 384

CURRENT_LLM_PROVIDER = LLMProvider.ai21

LOG_ALL_REQUESTS = True

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "logstash": {
            "level": "INFO",
            "class": "logstash.TCPLogstashHandler",
            "host": LOGSTASH_HOST,
            "port": LOGSTASH_PORT,
        },
    },
    "loggers": {
        "api_logger": {
            "handlers": ["logstash"],
            "level": "INFO",
            "propagate": False,
        },
    },
}
