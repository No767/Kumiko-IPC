import json
import os
import uuid
from datetime import datetime
from pathlib import Path

import pika
from dotenv import load_dotenv

currPath = Path(__file__).parents[1]
envPath = os.path.join(str(currPath), "dramatiq_ipc", ".env")
load_dotenv(dotenv_path=envPath)

IPC_SECRET_KEY = os.getenv("IPC_SECRET_KEY")
RABBITMQ_USER = os.getenv("RABBITMQ_USER")
RABBITMQ_PASSWORD = os.getenv("RABBITMQ_PASSWORD")
RABBITMQ_HOST = os.getenv("RABBITMQ_HOST")
RABBITMQ_PORT = os.getenv("RABBITMQ_PORT")
CONNECTION_URI = (
    f"amqp://{RABBITMQ_USER}:{RABBITMQ_PASSWORD}@{RABBITMQ_HOST}:{RABBITMQ_PORT}/"
)

body = json.dumps(
    {
        "queue_name": "default",
        "actor_name": "testing",
        "args": [],
        "kwargs": {},
        "options": {},
        "message_id": f"{str(uuid.uuid4())}",
        "message_timestamp": f"{datetime.utcnow().timestamp()}",
    }
)
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host=RABBITMQ_HOST,
        port=RABBITMQ_PORT,
        credentials=pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASSWORD),
    )
)
channel = connection.channel()
channel.basic_publish(exchange="", routing_key="default", body=body)
connection.close()
