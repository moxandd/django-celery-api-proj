from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "send_mate.settings")

app = Celery("send_mate")
app.conf.enable_utc = False

app.conf.update(timezone='Europe/Moscow')

app.config_from_object(settings, namespace="CELERY")

# Celery beat settings

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")