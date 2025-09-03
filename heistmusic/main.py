import os
import asyncio
from fastapi import FastAPI, Request
from pyrogram import Client, types
from dotenv import load_dotenv
import logging

# Load environment variables and set up logging
load_dotenv()
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
logging.basicConfig(level=logging.INFO)

app = FastAPI()
pyrogram_client = Client(
    "my_music_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    # This line loads all the Python files in the 'plugins' directory
    plugins=dict(root="app/plugins"),
)

# Startup event to start the Pyrogram client
@app.on_event("startup")
async def startup_event():
    await pyrogram_client.start()
    logging.info("Pyrogram client started.")

# Process the incoming webhook update
@app.post(f"/webhook/{BOT_TOKEN}")
async def process_webhook(request: Request):
    update_data = await request.json()
    asyncio.create_task(handle_update(update_data))
    return {"status": "ok"}

async def handle_update(update_data: dict):
    # Pyrogram can handle raw updates.
    # Deserialize the update into a Pyrogram Update object
    update = types.Update.parse(update_data, pyrogram_client)
    # The plugins will automatically handle the message
