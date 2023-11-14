from django.apps import apps
from django.contrib import admin

from qux.admin import QuxModelAdmin

excluded = []

app = apps.get_app_config("quxapp")
app_models = [x for x in app.get_models("quxapp") if x not in excluded]
for model in app_models:
    admin.site.register(model, QuxModelAdmin)
