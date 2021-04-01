from __future__ import absolute_import, unicode_literals
from django.conf import settings

import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mymo.settings')

app = Celery('mymo')

app.config_from_object(settings, namespace='CELERY')

app.autodiscover_tasks()
app.conf.update(CELERY_REDIS_MAX_CONNECTIONS=20,)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
