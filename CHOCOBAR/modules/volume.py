import os
from pyrogram import filters
from pyrogram.types import Message
from CHOCOBAR import app, pytg
from pyrogram import Client, filters
from pyrogram.types import Message
from pytgcalls.types import AudioQuality
from pytgcalls.types import VideoQuality
from pytgcalls import PyTgCalls, idle
from pytgcalls.types import MediaStream
from config import OWNER_ID

@app.on_message(filters.regex('volume (\d+)') & filters.user(OWNER_ID))
async def vol(client, message):
    volume_level = int(message.matches[0].group(1))
    chat_id=message.chat.id
    await pytg.change_volume_call(chat_id,volume_level)
    await message.reply_text(text=volume_level)
