import os
from pyrogram import Client, filters, types
from dotenv import load_dotenv

# Load environment variables to check for sudo users
load_dotenv()
SUDO_USERS = [int(u) for u in os.getenv("SUDO_USERS").split()]

@Client.on_message(filters.command("restart") & filters.user(SUDO_USERS))
async def restart_command_plugin(client: Client, message: types.Message):
    """Restarts the bot."""
    await message.reply("Restarting...")
    os.system("kill 1") # A simple way to trigger a restart on Render

@Client.on_message(filters.command("ping"))
async def ping_command_plugin(client: Client, message: types.Message):
    """Responds with pong."""
    await message.reply("Pong!")
