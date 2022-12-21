from celery import Celery

from celery_ipc import celeryconfig

app = Celery("ipc")
app.config_from_object(celeryconfig)
