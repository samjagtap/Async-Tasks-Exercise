import os
from celery import Celery


# set default Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

app = Celery("myproject")

# load settings from Django settings.py with CELERY_ prefix
app.config_from_object("django.conf:settings", namespace="CELERY")

# auto-discover tasks.py in apps
app.autodiscover_tasks()
