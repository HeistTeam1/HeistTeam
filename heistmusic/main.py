# app/main.py
import os
import asyncio
import logging
from fastapi import FastAPI, Request
from pyrogram import Client
from pyrogram.types import Message, Update
from dotenv import load_dotenv

# Import bot logic
from .music_player import play_music, stop_music

# Configure logging
logging.basicConfig(level=logging.INFO)

# Load environment variables
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")

app = FastAPI(docs_url="/docs")
pyrogram_client = Client("my_music_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Start the pyrogram client in a background task
@app.on_event("startup")
async def startup_event():
    await pyrogram_client.start()
    logging.info("Pyrogram client started.")
    
# Process the incoming webhook update
@app.post(f"/webhook/{BOT_TOKEN}")
async def process_webhook(request: Request):
    update_data = await request.json()
    
    # Process updates in the background
    asyncio.create_task(handle_update(update_data))
    
    return {"status": "ok"}

async def handle_update(update_data: dict):
    # Pyrogram can handle raw updates.
    # Deserialize the update into a Pyrogram Update object
    update = Update.parse(update_data, Client)
    
    if update.message:
        message = update.message
        
        # Simple command routing
        if message.text and message.text.startswith('/play'):
            query = message.text.split(' ', 1) if len(message.text.split(' ', 1)) > 1 else None
            if query:
                await play_music(pyrogram_client, message, query[0])
            else:
                await pyrogram_client.send_message(message.chat.id, "Please provide a song to play.")
        elif message.text == '/stop':
            await stop_music(pyrogram_client, message)
        else:
            await pyrogram_client.send_message(message.chat.id, "Hello! I am a music bot.")

# Set the webhook URL on bot startup (this is an example of how you would do it)
# In production, this can be a manual curl command or a one-time function
# @app.on_event("startup")
# async def set_webhook_url():
#     # You would use the Render domain name here
#     WEBHOOK_URL = f"https://your-render-app.onrender.com/webhook/{BOT_TOKEN}"
#     async with pyrogram_client as client:
#         await client.set_webhook(WEBHOOK_URL)
#         print(f"Webhook set to {WEBHOOK_URL}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
