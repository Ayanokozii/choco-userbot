import time
import random
from pyrogram import Client, filters
from CHOCOBAR import app

@app.on_message(filters.command("start"))
async def start(client, message):
  await message.reply_text(f"Hello !\nI am CHOCOBAR USERBOT")

  