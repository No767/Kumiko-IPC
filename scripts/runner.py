from celery_ipc.tasks import create_embed

print(
    create_embed(channel_id=454357482102587393, embed_content={"title": "Hello World!"})
)
