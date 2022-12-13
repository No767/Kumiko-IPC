from celery import Celery
# from . import config

app = Celery("tasks")
app.config_from_object("kumiko_ipc.config")

@app.task
def add(x, y):
    return x + y
