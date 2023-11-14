import os

from django.conf import settings


def default_project_setting_to_app(setting, default):
    return getattr(settings, setting, os.getenv(setting, default))


def default_app_setting_to_project(setting, default):
    return os.getenv(setting, getattr(settings, setting, default))


QUXAPP_SETTING="Qux"

# Examples
DATA_DIR = default_project_setting_to_app("DATA_DIR", "/dev/null")
NUM_DAYS = default_app_setting_to_project("NUM_DAYS", 1000)
