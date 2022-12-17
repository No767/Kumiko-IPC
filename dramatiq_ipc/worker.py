import asyncio
import os

import dramatiq
from discord.ext.ipc import Client
from dotenv import load_dotenv
from dramatiq.brokers.rabbitmq import RabbitmqBroker

load_dotenv()

IPC_SECRET_KEY = os.getenv("IPC_SECRET_KEY")
RABBITMQ_USER = os.getenv("RABBITMQ_USER")
RABBITMQ_PASSWORD = os.getenv("RABBITMQ_PASSWORD")
RABBITMQ_HOST = os.getenv("RABBITMQ_HOST")
RABBITMQ_PORT = os.getenv("RABBITMQ_PORT")
CONNECTION_URI = (
    f"amqp://{RABBITMQ_USER}:{RABBITMQ_PASSWORD}@{RABBITMQ_HOST}:{RABBITMQ_PORT}/"
)

ipc = Client(secret_key=IPC_SECRET_KEY)
rabbitmq_broker = RabbitmqBroker(url=CONNECTION_URI)
dramatiq.set_broker(rabbitmq_broker)


@dramatiq.actor(priority=10)
def request_user_data(user_id: int):
    asyncio.run(ipc.request("get_user_data", user_id=user_id))


@dramatiq.actor(priority=5)
def create_embed(channel_id: int, embed_content: dict):
    asyncio.run(
        ipc.request("create_embed", channel_id=channel_id, embed_content=embed_content)
    )


@dramatiq.actor(priority=0)
def testing(args):
    print(f"testing {args}")
