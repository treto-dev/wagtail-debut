import os
from typing import Optional

from pipit.settings import get_env, get_env_bool


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Version, be sure to bump this with each release (please follow semver.org)
APP_VERSION = "{{cookiecutter.version}}"

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# This is when debug is off, else django wont allow you to visit the site
ALLOWED_HOSTS = get_env("ALLOWED_HOSTS").split(",")

INTERNAL_IPS = ("127.0.0.1",)


# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",
    "django.contrib.gis",
    # Third party apps
    "storages",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail.core",
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.contrib.modeladmin",
    "wagtail.contrib.routable_page",
    "wagtail.contrib.settings",
    "modelcluster",
    "taggit",
    "wagtailfontawesome",
    "wagtail_meta_preview",
    "wagtail_headless_preview",
    "rest_framework",

    {% if cookiecutter.use_django_pattern_library == "yes" %}# Pattern library
    "pattern_library",{% endif %}

    {% if cookiecutter.use_grapple == "yes" %}# Grapple
    "grapple",
    "graphene_django",{% endif %}

    # Project specific apps
    "pipit",
    "sitesettings",
    "customuser",
    "customimage",
    "customdocument",
    "main",
    {% if cookiecutter.use_decoupled_frontend == "yes" %}"nextjs",{% endif %}
]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
]

ROOT_URLCONF = "pipit.urls"
APPEND_SLASH = True

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
        "OPTIONS": {
            "debug": DEBUG,
            "loaders": [
                "django.template.loaders.filesystem.Loader",
                "django.template.loaders.app_directories.Loader",
            ],
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "wagtail.contrib.settings.context_processors.settings",
                # Project specific
                "pipit.context_processors.settings_context_processor",
            ],
            {% if cookiecutter.use_django_pattern_library == "yes" %}"builtins": [
                "pattern_library.loader_tags"
            ],{% endif -%}
        },
    }
]

WSGI_APPLICATION = "pipit.wsgi.application"


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
# Using PostgreSQL
DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": get_env("DATABASE_NAME"),
        "USER": get_env("DATABASE_USER"),
        "PASSWORD": get_env("DATABASE_PASSWORD"),
        "HOST": get_env("DATABASE_HOST"),
        "PORT": get_env("DATABASE_PORT", default=5432),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"  # NOQA
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},  # NOQA
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},  # NOQA
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"  # NOQA
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/
TIME_ZONE = "Europe/Paris"
LANGUAGE_CODE = "fr-fr"
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True
LOCALE_PATHS = [os.path.join(BASE_DIR, "locale")]

# Email
DEFAULT_FROM_EMAIL = get_env("DEFAULT_FROM_EMAIL", default="noreply@example.com")

# Auth
AUTH_USER_MODEL = "customuser.User"

# Wagtail
WAGTAIL_SITE_NAME = "{{ cookiecutter.project_name }}"
WAGTAILIMAGES_IMAGE_MODEL = "customimage.CustomImage"
WAGTAILDOCS_DOCUMENT_MODEL = "customdocument.CustomDocument"
WAGTAIL_ALLOW_UNICODE_SLUGS = False

WAGTAILIMAGES_FORMAT_CONVERSIONS = {
    "png": "jpeg",
    "webp": "webp",
}

# File storage
if get_env("AWS_ACCESS_KEY_ID", ""):
    AWS_ACCESS_KEY_ID = get_env("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = get_env("AWS_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = get_env("AWS_BUCKET_NAME")

    AWS_QUERYSTRING_AUTH = False
    AWS_S3_FILE_OVERWRITE = False

    AWS_EXPIRY = 60 * 60 * 24 * 7  # One week
    AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age={}".format(AWS_EXPIRY)}

    DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
    THUMBNAIL_DEFAULT_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"


# Uploaded media
MEDIA_URL = "/wt/media/"
MEDIA_ROOT = get_env("MEDIA_PATH")


# Static files, if in production use static root, else use static dirs

# Static URL to use when referring to static files located in STATIC_ROOT.
STATIC_URL = "/wt/static/"

# The absolute path to the directory where collectstatic will collect static
# files for deployment. Example: "/var/www/example.com/static/"I
STATIC_ROOT = get_env("STATIC_PATH")

# This setting defines the additional locations the staticfiles will traverse
STATICFILES_DIRS = (
    # "/home/special.polls.com/polls/static",
    # "/home/polls.com/polls/static",
)

# Prevent content type sniffing
SECURE_CONTENT_TYPE_NOSNIFF = True

# Admin
ADMIN_URL = "wt/admin/"

# NextJS
HEADLESS_PREVIEW_CLIENT_URLS = {
    "default": "/api/preview/",
}

# Sentry
SENTRY_DSN: Optional[str] = None
SENTRY_ENVIRONMENT: Optional[str]= None


{% if cookiecutter.use_grapple == "yes" %}# Grapple Config:
GRAPHENE = {"SCHEMA": "grapple.schema.schema"}
GRAPPLE_APPS = {
    "home": ""
}{% endif %}

{% if cookiecutter.use_django_pattern_library == "yes" %}# Pattern Library
PATTERN_LIBRARY = {
    # Groups of templates for the pattern library navigation. The keys
    # are the group titles and the values are lists of template name prefixes that will
    # be searched to populate the groups.
    "SECTIONS": (
        ("components", ["patterns/components"]),
        ("pages", ["patterns/pages"]),
    ),

    # Configure which files to detect as templates.
    "TEMPLATE_SUFFIX": ".html",

    # Set which template components should be rendered inside of,
    # so they may use page-level component dependencies like CSS.
    "PATTERN_BASE_TEMPLATE_NAME": "patterns/base.html",

    # Any template in BASE_TEMPLATE_NAMES or any template that extends a template in
    # BASE_TEMPLATE_NAMES is a "page" and will be rendered as-is without being wrapped.
    "BASE_TEMPLATE_NAMES": ["patterns/base_page.html"],
}{% endif %}
