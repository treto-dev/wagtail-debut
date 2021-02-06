"""
Write local settings here, or override base settings
"""
from pipit.settings.base import *  # NOQA
from django.apps import apps


VS_CODE_REMOTE_DEBUG = get_env_bool("VS_CODE_REMOTE_DEBUG", default=False)
DEBUG = True
TEMPLATES[0]["OPTIONS"]["debug"] = DEBUG  # type: ignore[index]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Allow weak local passwords
AUTH_PASSWORD_VALIDATORS = []

INTERNAL_IPS = get_env("INTERNAL_IPS", default="").split(",")

# Add django debug toolbar when using local version
if get_env_bool("DEBUG_TOOLBAR", default=True):
    DEBUG_TOOLBAR_PATCH_SETTINGS = False

    INSTALLED_APPS += ["debug_toolbar"]

    MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

    DEBUG_TOOLBAR_CONFIG = {
        "SHOW_TOOLBAR_CALLBACK": "pipit.settings.local.show_toolbar"
    }


{% if cookiecutter.use_grapple %}HEADLESS_PREVIEW_CLIENT_URLS = {
    "default": "http://localhost:3000/api/preview/",
}{% endif %}

{% if cookiecutter.use_decoupled_frontend%}INSTALLED_APPS += ["corsheaders"]
MIDDLEWARE = ["corsheaders.middleware.CorsMiddleware"] + MIDDLEWARE
CORS_ORIGIN_ALLOW_ALL = True{% endif %}

# Allow django-debug-bar under docker
def show_toolbar(request):
    return True
