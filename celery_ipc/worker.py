from celery import Celery

app = Celery("ipc")
app.config_from_object("celeryconfig")
