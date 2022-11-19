import asyncio
import os

from aio_pika import ExchangeType, connect
from aio_pika.abc import AbstractIncomingMessage
from discord.ext.ipc import Client
from dotenv import load_dotenv

load_dotenv()

IPC_SECRET_KEY = os.getenv("IPC_Secret_Key")
RABBITMQ_USERNAME = os.getenv("RabbitMQ_Username")
RABBITMQ_PASSWORD = os.getenv("RabbitMQ_Password")
RABBITMQ_HOST = os.getenv("RabbitMQ_Host")
CONNECTION_URI = f"amqp://{RABBITMQ_USERNAME}:{RABBITMQ_PASSWORD}@{RABBITMQ_HOST}/"
ipc = Client(secret_key=IPC_SECRET_KEY)


async def on_message(message: AbstractIncomingMessage) -> None:
    async with message.process():
        mainMessage = message.body.decode("utf-8")
        listOfWords = mainMessage.split(":")
        await ipc.request(str(listOfWords[0]), user_id=int(listOfWords[1]))


async def main() -> None:
    # Perform connection
    connection = await connect(CONNECTION_URI)

    async with connection:
        # Creating a channel
        channel = await connection.channel()
        await channel.set_qos(prefetch_count=1)

        logs_exchange = await channel.declare_exchange(
            "ipc",
            ExchangeType.DIRECT,
        )

        # Declaring queue
        queue = await channel.declare_queue(durable=True)

        # Binding the queue to the exchange
        await queue.bind(logs_exchange, routing_key="info")

        print(" [*] Waiting for logs. To exit press CTRL+C")

        async with queue.iterator() as iterator:
            message: AbstractIncomingMessage
            async for message in iterator:
                async with message.process():
                    print(f" [x] {message.body!r}")

        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
