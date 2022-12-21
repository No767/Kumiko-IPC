import asyncio
import os

from discord.ext.ipc import Client

from celery_ipc import worker

IPC_SECRET_KEY = os.getenv("IPC_SECRET_KEY")

ipc = Client(secret_key=IPC_SECRET_KEY)

from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@worker.app.task
def request_user_data(user_id: int) -> None:
    asyncio.run(ipc.request("get_user_data", user_id=user_id))


@worker.app.task
def create_embed(channel_id: int, embed_content: dict) -> None:
    asyncio.run(
        ipc.request("create_embed", channel_id=channel_id, embed_content=embed_content)
    )


@worker.app.task
def testing(arg) -> None:
    logger.info(arg)
