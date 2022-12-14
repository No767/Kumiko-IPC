import asyncio
import os

from discord.ext.ipc import Client
from worker import app

IPC_SECRET_KEY = os.getenv("IPC_SECRET_KEY")

ipc = Client(secret_key=IPC_SECRET_KEY)


@app.task
def request_user_data(user_id: int) -> None:
    asyncio.run(ipc.request("get_user_data", user_id=user_id))


@app.task
def create_embed(channel_id: int, embed_content: dict) -> None:
    asyncio.run(
        ipc.request("create_embed", channel_id=channel_id, embed_content=embed_content)
    )
