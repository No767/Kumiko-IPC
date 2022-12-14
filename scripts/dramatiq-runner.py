from dramatiq_ipc.worker import create_embed, request_user_data

request_user_data.send(user_id=454357482102587393)
create_embed.send(
    channel_id=454357482102587393, embed_content={"title": "Hello World!"}
)
