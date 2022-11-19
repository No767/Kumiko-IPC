import asyncio
import os

from aio_pika import DeliveryMode, ExchangeType, Message, connect
from dotenv import load_dotenv

load_dotenv()

RABBITMQ_USERNAME = os.getenv("RabbitMQ_Username")
RABBITMQ_PASSWORD = os.getenv("RabbitMQ_Password")
RABBITMQ_HOST = os.getenv("RabbitMQ_Host")
CONNECTION_URI = f"amqp://{RABBITMQ_USERNAME}:{RABBITMQ_PASSWORD}@{RABBITMQ_HOST}/"


async def main() -> None:
    # Perform connection
    connection = await connect(CONNECTION_URI)

    async with connection:
        # Creating a channel
        channel = await connection.channel()

        logs_exchange = await channel.declare_exchange(
            "logs_main",
            ExchangeType.DIRECT,
        )

        # message_body = (
        #     b" ".join(arg.encode() for arg in sys.argv[1:]) or b"get_user_data:454357482102587393"
        # )

        message_body = b"get_user_data:454357482102587393"

        message = Message(
            message_body,
            delivery_mode=DeliveryMode.PERSISTENT,
        )

        # Sending the message
        await logs_exchange.publish(message, routing_key="info")

        print(f" [x] Sent {message!r}")


if __name__ == "__main__":
    asyncio.run(main())
