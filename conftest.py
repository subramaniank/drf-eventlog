import django
import pytest
from django.db import models

from django.conf import settings

import os

DEFAULT_SETTINGS = dict(
    INSTALLED_APPS=(
        "django.contrib.contenttypes",
        "rest_framework",
        "django_filters",
        "drf_eventlog",
        "drf_eventlog.tests"
    ),
    MIDDLEWARE_CLASSES=(),
    DATABASES={
        "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME":"drf_eventlog"
        }
    },
    SITE_ID=1,
    ROOT_URLCONF="drf_eventlog.tests.urls",
    SECRET_KEY="notasecret",
)

if not settings.configured:
        settings.configure(**DEFAULT_SETTINGS)

django.setup()
