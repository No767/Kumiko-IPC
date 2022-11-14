import os

from discord.ext.ipc import Client
from dotenv import load_dotenv
from quart import Quart

load_dotenv()

app = Quart(__name__)
ipc = Client(secret_key=os.getenv("IPC_Secret_Key"))


@app.route("/")
async def main():
    return await ipc.request("get_user_data", user_id=454357482102587393)


if __name__ == "__main__":
    app.run(debug=False)
