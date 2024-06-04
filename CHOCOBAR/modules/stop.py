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



@app.on_message(filters.regex('.stop') & filters.user(OWNER_ID))
async def stop_handler(_: Client, message: Message):
  await message.reply_text(text="Userbot  stopped song.")
  await pytg.leave_group_call(message.chat.id, )
