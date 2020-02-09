"""
@file: celery.py
@author: rrh
@time: 2020/2/9 3:21 下午
"""

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celerytest.settings')

app = Celery('celerytest')

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks('celerytest')


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

