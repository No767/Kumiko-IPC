import asyncio

from aio_pika import ExchangeType, connect
from aio_pika.abc import AbstractIncomingMessage


async def on_message(message: AbstractIncomingMessage) -> None:
    async with message.process():
        messageContent = message.body
        parsedMessageContent = messageContent.decode("utf-8")
        print(f"[x] {parsedMessageContent!r}")


class RMQService:
    def __init__(self, uri: str):
        self.self = self
        self.uri = uri

    async def init(self):
        connection = await connect(self.uri)

        async with connection:
            # Creating a channel
            channel = await connection.channel()
            await channel.set_qos(prefetch_count=1)

            logs_exchange = await channel.declare_exchange(
                "logs",
                ExchangeType.FANOUT,
            )

            # Declaring queue
            queue = await channel.declare_queue(exclusive=True)

            # Binding the queue to the exchange
            await queue.bind(logs_exchange)

            # Start listening the queue
            await queue.consume(on_message)

            print(" [*] Waiting for logs. To exit press CTRL+C")
            await asyncio.Future()
